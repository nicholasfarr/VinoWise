import streamlit as st
import pandas as pd

# Load data once
## NEED TO UPDATE AND USE IN HOUSE FUNCTIONS
@st.cache_data
def load_wine_data():
    df = pd.read_csv('DATA/winemag-data-130k-v2.csv', usecols=['title', 'country', 'price', 'points', 'description'])
    df.rename(columns={'title': 'name', 'points': 'score'}, inplace=True)
    df.dropna(subset=['name', 'country', 'price', 'score'], inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df

wine_data = load_wine_data()

st.title("🍷 Wine Recommender")

wine_name = st.text_input("Enter a wine you've tried and liked:")

if wine_name:
    match = wine_data[wine_data['name'].str.lower() == wine_name.lower()]
    if not match.empty:
        wine = match.iloc[0]
        st.success(f"Found: {wine['name']} ({wine['country']}) - ${wine['price']}, {wine['score']} pts")

        st.subheader("Recommended Similar Wines:")
        similar = wine_data[
            (wine_data['country'] == wine['country']) &
            (abs(wine_data['price'] - wine['price']) <= 5)
        ].sort_values(by='score', ascending=False).head(5)

        for _, row in similar.iterrows():
            st.markdown(f"**{row['name']}** – ${row['price']} – {row['score']} pts")

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