import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from data_loader import load_data

st.set_page_config(page_title="🎬 Meta Score", layout="wide")

df = load_data()

st.header("📈 Meta Score Analysis")


min_meta, max_meta = st.slider(
    "Specify the Meta Score range:", 
    int(df['meta_score'].min()), 
    int(df['meta_score'].max()), 
    (50, 90)
)


filtered_meta = df[(df['meta_score'] >= min_meta) & (df['meta_score'] <= max_meta)]


with st.expander(f"🎬 Movies with Meta Score between {min_meta}-{max_meta}"):
    st.dataframe(filtered_meta[['series_title','meta_score','imdb_rating']])

avg_meta = filtered_meta['meta_score'].mean()
st.metric("⭐ Average Meta Score in Range", f"{avg_meta:.2f}")


st.subheader("📊 Meta Score Histogram")
fig, ax = plt.subplots(figsize=(8,4))
sns.histplot(df['meta_score'], bins=20, kde=True, color="orange", ax=ax)
ax.set_xlabel("Meta Score")
ax.set_ylabel("Count")
ax.set_title("Distribution of Meta Scores")
st.pyplot(fig)

# Insight
st.markdown("**Insight:** Most movies have Meta Scores between 60–80, indicating that critically well-received films cluster in this range.")
