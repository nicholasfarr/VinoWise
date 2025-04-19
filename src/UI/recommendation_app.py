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

st.title("🍷 Wine Recommender")

with st.form(key="search_form"):
    wine_name = st.text_input("Enter a wine you've tried and liked:")
    amount = st.number_input("Number of recommendations:", min_value=1, max_value=50, value=5)
    submitted = st.form_submit_button("🔍 Search")

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


    else:
        st.warning("Wine not found. Enter the country and price range for recommendations.")
        country = st.text_input("Country")
        price = st.number_input("Approximate Price ($)", min_value=0.0, step=1.0)

        if country and price:
            results = wine_data[
                (wine_data['country'].str.lower() == country.lower()) &
                (abs(wine_data['price'] - price) <= 5)
            ].sort_values(by='score', ascending=False).head(5)

            if results.empty:
                st.error("No matches found.")
            else:
                st.subheader("Recommended Wines:")
                for _, row in results.iterrows():
                    st.markdown(f"**{row['name']}** – ${row['price']} – {row['score']} pts")