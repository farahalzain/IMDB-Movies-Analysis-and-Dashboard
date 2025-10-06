import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from data_loader import load_data

st.set_page_config(page_title="📊 Overview", layout="wide")

# Load data
df = load_data()


st.markdown("## 🎯 Key Insights")
col1, col2, col3, col4 = st.columns(4)

with col1:
    avg_rating = df["imdb_rating"].mean().round(2)
    st.metric("⭐ Avg Rating", avg_rating)

with col2:
    highest_gross = df.loc[df["gross"].idxmax()]
    st.metric("💰 Highest Gross", highest_gross["series_title"].iloc[0])
    

with col3:
    top_director = df['director'].value_counts().idxmax()
    st.metric("🎬 Top Director", top_director)

with col4:
    most_common_genre = df["genre"].value_counts().idxmax()
    st.metric("🎭 Top Genre", most_common_genre)

# -------------------------
# 🔹 Distributions
# -------------------------
st.markdown("## 📊 Distributions")

col1, col2 = st.columns(2)

with col1:
    selected_rating = st.slider("Filter Ratings", 
                                float(df["imdb_rating"].min()), 
                                float(df["imdb_rating"].max()), 
                                (7.0, 9.0))
    filtered_df = df[(df["imdb_rating"] >= selected_rating[0]) & 
                    (df["imdb_rating"] <= selected_rating[1])]
    fig, ax = plt.subplots()
    sns.histplot(filtered_df["imdb_rating"], bins=20, color='skyblue', ax=ax)
    ax.set_title("IMDb Rating Distribution")
    st.pyplot(fig)
    st.markdown("**Insight:** Most movies fall between 7–8 rating range.")

with col2:
    top_n = st.slider("Show Top N Gross Movies", 5, 20, 10)
    top_gross_movies = df.nlargest(top_n, "gross")
    fig, ax = plt.subplots()
    sns.barplot(x="gross", y="series_title", data=top_gross_movies, palette="Greens_r", ax=ax)
    ax.set_title(f"Top {top_n} Grossing Movies")
    st.pyplot(fig)
    st.markdown("**Insight:** Revenues are dominated by modern blockbuster franchises.")


st.markdown("## 👨‍🎨 Directors & Stars")

col1, col2 = st.columns(2)

with col1:
    top_n_dir = st.selectbox("Select Top N Directors", [5, 10, 15], index=1)
    top_directors = df['director'].value_counts().head(top_n_dir)
    fig, ax = plt.subplots(figsize=(7,4))
    sns.barplot(x=top_directors.values, y=top_directors.index, palette="magma", ax=ax)
    ax.set_title(f"Top {top_n_dir} Directors")
    st.pyplot(fig)

with col2:
    all_stars = pd.concat([df['star1'], df['star2'], df['star3'], df['star4']])
    top_n_stars = st.selectbox("Select Top N Stars", [5, 10, 15], index=1)
    top_stars = all_stars.value_counts().head(top_n_stars)
    fig, ax = plt.subplots(figsize=(7,4))
    sns.barplot(x=top_stars.values, y=top_stars.index, palette="coolwarm", ax=ax)
    ax.set_title(f"Top {top_n_stars} Stars")
    st.pyplot(fig)


st.markdown("## 🎬 Certificates, Runtime, Meta Score")

col1, col2, col3 = st.columns(3)

with col1:
    fig, ax = plt.subplots()
    sns.countplot(x="certificate", data=df, palette="Set2", ax=ax)
    plt.xticks(rotation=45)
    ax.set_title("Certificate Counts")
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots()
    sns.histplot(df["runtime"], bins=30, kde=True, color="blue", ax=ax)
    ax.set_title("Runtime Distribution")
    st.pyplot(fig)

with col3:
    fig, ax = plt.subplots()
    sns.histplot(df["meta_score"], bins=30, kde=True, color="red", ax=ax)
    ax.set_title("Meta Score Distribution")
    st.pyplot(fig)


st.markdown("## 📊 Extra Stats")
col1, col2, col3, col4 = st.columns(4)

col1.metric("🎞️ Total Movies", len(df))
col2.metric("📅 Earliest Movie", int(df["released_year"].min()))
col3.metric("🆕 Latest Movie", int(df["released_year"].max()))
col4.metric("🎯 Avg Meta Score", df["meta_score"].mean().round(2))
