import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_loader import load_data

st.set_page_config(page_title="🎭 Genres", layout="wide")
df = load_data()

st.header("🎭 Genres Analysis")

selected_genre = st.selectbox("Choose a Genre:", df["genre"].unique())


option = st.radio("Select Analysis Type:", 
                ("🎥 Show Movies", "⭐ Rating Distribution"))

if option == "🎥 Show Movies":
    st.subheader(f"Movies in {selected_genre} Genre")
    st.dataframe(df[df["genre"] == selected_genre][["series_title", "imdb_rating", "gross"]])

elif option == "⭐ Rating Distribution":
    st.subheader(f"Rating Distribution for {selected_genre}")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(df[df["genre"] == selected_genre]["imdb_rating"], bins=10, kde=True, color="skyblue", ax=ax)
    ax.set_xlabel("IMDB Rating")
    ax.set_ylabel("Count")
    st.pyplot(fig)

# Top 10 Genres
st.subheader("🏆 Top 10 Genres by Number of Movies")
top_10_genres = df["genre"].value_counts().head(10)

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=top_10_genres.values, y=top_10_genres.index, palette="pastel", ax=ax)
ax.set_xlabel("Number of Movies")
ax.set_ylabel("Genre")
st.pyplot(fig)

st.markdown("**Insight:** The most common genres are Drama, Crime, and Comedy, reflecting their universal appeal across audiences.")

