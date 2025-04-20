import streamlit as st
import pandas as pd

import sys
import os

#changing path so i can import modules from the src directory
#idk how else to do it
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from WineData import *
from WineSort import *


# Load data once
## NEED TO UPDATE AND USE IN HOUSE FUNCTIONS
@st.cache_data
def load_wine_data(): #caching the data so we dont have to load it every time
    return load_wine_nodes()

wine_data = load_wine_data()

#used html instead of st.title to because i couldnt center them and size em properly
st.markdown(
    "<h1 style='text-align: center;'>🍷 Wine Recommender</h1>",
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)
with col1:
    st.markdown(
    "<h5 style='text-align: center; margin-bottom: 10px;'>Find similar wines by name</h5>",
    unsafe_allow_html=True)
    with st.form(key="search_form"):
        wine_name = st.text_input("Enter a wine you've tried and liked:")
        amount = st.number_input("Number of recommendations:", min_value=1, max_value=50, value=5)
        submitted = st.form_submit_button("🔍 Search")
with col2:
    st.markdown(
    "<h5 style='text-align: center; margin-bottom: 10px;'>Or by country + price</h5>",
    unsafe_allow_html=True)
    with st.form(key="fallback_form"):
        price = st.number_input("Approximate Price ($):", min_value=0.0, step=1.0)
        fallback_amount = st.number_input("Number of fallback recommendations:", min_value=1, max_value=50, value=5)
        fallback_submit = st.form_submit_button("🍷 Search by Price")
st.markdown("---")


if submitted:
    node = findWineByName(wine_data, wine_name)
    if node:
        st.success(f"Found: {node.title} ({node.country}) - ${node.price}, {node.points} pts")

        createSimilarityScoreDict(wine_data, node)
        st.subheader("Recommended Similar Wines:")

        recs, sort_time = findRecommendationsMerge(node, amount)  #merge
        recsQUICK, sort_timeQUICK = findRecommendationsQuick(node, amount)  #quick

        if(recs != recsQUICK):
            st.error("Recommendations do not match between sorting algorithms. ALGOS SHOULD BE INSPECTED.")
        for neighbor, score in recs:
            st.markdown(f"**{neighbor.title}** – ${neighbor.price} (Comparison percentage: {score * 100:.2f}%)")

        st.caption(f"Merge sorted in {sort_time:.4f} seconds\nQuick sorted in {sort_timeQUICK:.4f} seconds")
        st.write(f"### Additional Information for {node.title}:")
        st.write(f"**Description:** {node.description}")
        st.write(f"**Winery:** {node.winery}")
        st.write(f"**Variety:** {node.variety}")
        st.write(f"**Keywords:** {', '.join(node.keywords)}")



if fallback_submit:
    fallback = [
        n for n in wine_data
        if abs(n.price - price) <= 5
    ]
    fallback.sort(key=lambda x: (-x.points, x.title))

    if fallback:
        st.subheader("Recommendations based on price:")
        for n in fallback[:fallback_amount]:
            st.markdown(f"**{n.title}** – ${n.price} ({n.points} pts)")
    else:
        st.error("No recommendations found based on this price.")