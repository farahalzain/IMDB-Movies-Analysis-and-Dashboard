import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from data_loader import load_data

st.set_page_config(page_title="🎬 Directors", layout="wide")

# Load data
df = load_data()

st.header("🎬 Directors Analysis")


director = st.selectbox("Choose a director:", df['director'].unique())


option = st.radio("Select Analysis Type:", 
                ("📽️ Show Movies", "⭐ Average Rating"))

if option == "📽️ Show Movies":
    st.subheader(f"Movies by {director}")
    st.dataframe(df[df['director'] == director][['series_title', 'imdb_rating', 'gross']])

elif option == "⭐ Average Rating":
    avg_rating = df[df['director'] == director]['imdb_rating'].mean()
    st.success(f"⭐ Average Rating for {director}: {avg_rating:.2f}")


st.subheader("🏆 Top 10 Directors by Number of Movies")
top_10_directors = df['director'].value_counts().head(10)

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=top_10_directors.values, y=top_10_directors.index, palette="Set3", ax=ax)
ax.set_xlabel("Number of Movies")
ax.set_ylabel("Director")
st.pyplot(fig)
st.markdown("**Insight:** Legendary directors such as Alfred Hitchcock, Steven Spielberg, and Martin Scorsese dominate the top list, showing the influence of renowned filmmakers on cinema history.")