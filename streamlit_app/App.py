import streamlit as st

st.set_page_config(page_title="🎬 IMDB Movies Dashboard", layout="wide")

# Title
st.title("🎬 IMDB Movies Dashboard")


st.markdown("""
### 👋 Welcome!
This interactive dashboard allows you to explore **IMDB Movies Dataset** in depth.  
You can analyze the top-rated movies and their patterns across different aspects such as **Genres, Ratings, Directors, Stars, and Earnings**.
""")

st.subheader("📂 About the Dataset")
st.markdown("""
- 🎞️ Contains thousands of top IMDB movies.  
- 📊 Includes **Gross Earnings, Ratings, Meta Scores, Runtime, Genres, Directors, and Stars**.  
- 🕒 Covers a wide range of release years (from 1920s to 2020s).  
""")

st.subheader("🧭 How to Use the Dashboard")
st.markdown("""
- 👉 Use the **Sidebar Menu** to navigate between pages.  
- 🔍 Each page provides **interactive filters** (dropdowns, sliders, etc.) for custom exploration.  
- 📈 Visualizations update instantly with your selections.  
""")

st.subheader("🎯 Goals of the Project")
st.markdown("""
- Understand the relationship between **earnings & ratings**.  
- Explore the **impact of genres** on success.  
- Highlight **top directors and stars** shaping the industry.  
- Provide **insights for movie studios** on market trends.  
""")

st.info("⚡️ Tip: Start with the **Overview Page** to get a quick summary of the dataset!")

