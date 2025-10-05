import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from data_loader import load_data

st.set_page_config(page_title="🔗 Relationships", layout="wide")

df = load_data()

st.header("🔗 Relationships Between Features")

# Gross vs IMDb
st.subheader("💰 Gross vs ⭐ IMDB Rating")
fig, ax = plt.subplots()
sns.scatterplot(x="imdb_rating", y="gross", data=df, alpha=0.6, ax=ax)
ax.set_xlabel("IMDb Rating")
ax.set_ylabel("Gross")
st.pyplot(fig)
st.markdown("**Insight:** Weak positive correlation; higher ratings slightly relate to higher gross revenue.")

# Runtime vs IMDb
st.subheader("⏱️ Runtime vs ⭐ IMDB Rating")
fig, ax = plt.subplots()
sns.scatterplot(x="runtime", y="imdb_rating", data=df, alpha=0.6, color="orange", ax=ax)
ax.set_xlabel("Runtime (min)")
ax.set_ylabel("IMDb Rating")
st.pyplot(fig)
st.markdown("**Insight:** No strong relationship; movie length doesn't significantly affect ratings.")

# Meta Score vs IMDb
st.subheader("📈 Meta Score vs ⭐ IMDB Rating")
fig, ax = plt.subplots()
sns.regplot(x='meta_score', y='imdb_rating', data=df, scatter_kws={'alpha':0.6}, color="green", ax=ax)
ax.set_xlabel("Meta Score")
ax.set_ylabel("IMDb Rating")
st.pyplot(fig)
st.markdown("**Insight:** Moderate positive correlation; higher Meta Scores usually correspond to higher IMDb ratings.")

# Correlation Heatmap
st.subheader("🔥 Correlation Heatmap")
fig, ax = plt.subplots(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)
st.markdown("**Insight:** Shows correlations between numeric features. Ratings and gross show weak correlation; Meta Score is moderately correlated with IMDb Rating.")

# Average Gross per Year
st.subheader("💰 Average Gross by Year")
avg_gross_year = df.groupby('released_year')['gross'].mean().reset_index()
min_year, max_year = int(avg_gross_year['released_year'].min()), int(avg_gross_year['released_year'].max())

year_range = st.slider("Select Year Range", min_value=min_year, max_value=max_year, value=(min_year, max_year))
filtered = avg_gross_year[(avg_gross_year['released_year'] >= year_range[0]) &
                        (avg_gross_year['released_year'] <= year_range[1])]

fig, ax = plt.subplots(figsize=(12,6))
sns.lineplot(x='released_year', y='gross', data=filtered, marker='o', ax=ax)
ax.set_title("Average Gross by Year")
ax.set_ylabel("Average Gross")
ax.set_xlabel("Release Year")
plt.xticks(rotation=45)
st.pyplot(fig)
st.markdown("**Insight:** More recent movies tend to have higher gross earnings, reflecting global market growth and blockbuster franchises.")
