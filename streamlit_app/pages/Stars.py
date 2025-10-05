import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from data_loader import load_data

st.set_page_config(page_title="⭐ Stars", layout="wide")
df = load_data()

st.header("⭐ Stars Analysis")

all_stars = pd.concat([df['star1'], df['star2'], df['star3'], df['star4']])
top_10_stars = all_stars.value_counts().head(10)


star = st.selectbox("Choose a star:", all_stars.unique())

# Show Movies
with st.expander(f"🎥 Movies Featuring {star}"):
    movies_star = df[(df['star1']==star) | (df['star2']==star) | 
                    (df['star3']==star) | (df['star4']==star)][['series_title', 'imdb_rating', 'gross']]
    st.dataframe(movies_star)
    
    fig, ax = plt.subplots(figsize=(6,4))
    sns.histplot(movies_star['imdb_rating'], bins=10, kde=True, color='skyblue', ax=ax)
    ax.set_title(f"IMDB Rating Distribution for {star}")
    st.pyplot(fig)

avg_rating = movies_star['imdb_rating'].mean()
st.info(f"⭐ Average Rating for {star}: {avg_rating:.2f}")

st.subheader("📊 Top 10 Stars by Number of Movies")
fig, ax = plt.subplots(figsize=(8,5))
sns.barplot(x=top_10_stars.values, y=top_10_stars.index, palette="Set1", ax=ax)
ax.set_xlabel("Number of Movies")
ax.set_ylabel("Star")
ax.set_title("Top 10 Stars")
st.pyplot(fig)
st.markdown("**Insight:** Robert De Niro, Tom Hanks, and Al Pacino appear most frequently, highlighting their influence on popular cinema.")
