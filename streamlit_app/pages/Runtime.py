import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from data_loader import load_data

st.set_page_config(page_title="⏱️ Runtime", layout="wide")
df = load_data()

st.header("⏱️ Runtime Analysis")


min_runtime, max_runtime = st.slider(
    "Specify the duration (minutes):", 
    int(df['runtime'].min()), 
    int(df['runtime'].max()), 
    (90, 150)
)

filtered = df[(df['runtime'] >= min_runtime) & (df['runtime'] <= max_runtime)]

with st.expander(f"📽️ Movies with runtime between {min_runtime}-{max_runtime} mins"):
    st.dataframe(filtered[['series_title','runtime','imdb_rating']])


st.subheader("📊 Runtime Distribution")
fig, ax = plt.subplots(figsize=(8,4))
sns.histplot(df['runtime'], bins=20, kde=True, color="skyblue", ax=ax)
ax.set_xlabel("Runtime (minutes)")
ax.set_ylabel("Count")
ax.set_title("Distribution of Movie Runtime")
st.pyplot(fig)

# Insight
st.markdown("**Insight:** Most movies have a runtime between 100–150 minutes, which reflects standard feature-length films in the industry.")

