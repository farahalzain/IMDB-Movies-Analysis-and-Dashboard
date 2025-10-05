import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from data_loader import load_data

st.set_page_config(page_title="📜 Certificates", layout="wide")
df = load_data()

st.header("📜 Certificates Analysis")

certificate = st.selectbox("Choose a certificate:", df["certificate"].unique())

with st.expander(f"🎞️ Movies with Certificate {certificate}"):
    st.dataframe(df[df["certificate"] == certificate][['series_title', 'imdb_rating', 'gross']])

st.subheader("📊 Certificates Distribution")
fig, ax = plt.subplots(figsize=(8,4))
sns.countplot(x="certificate", data=df, palette="Set2", ax=ax)
plt.xticks(rotation=45)
ax.set_title("Certificate Counts")
st.pyplot(fig)
st.markdown("**Insight:** Most movies fall under certificates U, A, and UA, reflecting family-friendly and general-audience films dominance.")
