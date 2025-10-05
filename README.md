# 🎬 IMDB Movies Data Analysis & Streamlit Dashboard

## 📖 Project Overview

This project provides an in-depth **exploratory data analysis (EDA)** of the **IMDB Top 1000 Movies** dataset.
It explores patterns and relationships between movie attributes such as **IMDb rating, meta score, gross earnings, runtime, and genres**, revealing trends and insights about the global movie industry.

In addition, an **interactive Streamlit dashboard** was built to visualize and explore movie data dynamically.

---

## 🧰 Tech Stack

* **Python 3**
* **Pandas**, **NumPy** – for data cleaning and manipulation
* **Matplotlib**, **Seaborn**, **Plotly** – for visualization
* **Streamlit** – for building interactive dashboards
* **Google Colab / Jupyter Notebook** – for analysis

---

## 📂 Project Structure

```
IMDB-Movies-Analysis/
│
├── imdb_movies.ipynb          # Main data analysis notebook
├── streamlit_app/
|   ├── imdb_top_1000.csv          # Dataset file
│   ├── App.py
│   ├── pages
|       ├── Overview.py
|       ├── Meta_Score.py
│       ├── Relationships.py
|       ├── Certificates.py
|       ├── Directors.py
|       ├── Stars.py
|       ├── Runtime.py
|       ├── Genres.py    
│   └── data_loader.py         # Helper function to load dataset
│
└── README.md
```

---

## 🧹 Data Cleaning & Preprocessing

* Renamed columns to lowercase
* Removed unnecessary columns (`poster_link`, `overview`)
* Handled missing values (`gross`, `meta_score`, `certificate`, etc.)
* Converted data types (numeric conversion for `runtime`, `released_year`, `gross`)
* Exploded multi-genre columns for granular analysis

---

## 📊 Analysis & Visual Insights

### 🎞️ Distribution Insights

* **IMDb Rating:** Most movies rated between 7–8
* **Runtime:** Common range is 100–150 minutes
* **Certificates:** Family (U/UA) and adult (A/R) dominate
* **Genres:** Drama, Crime, and Comedy are most popular

### 💰 Top Movies, Directors, and Stars

* **Top Grossing Movies:** Major franchises like *Avengers*, *Batman*, *Star Wars*
* **Top Directors:** *Alfred Hitchcock*, *Steven Spielberg*, *Martin Scorsese*
* **Top Stars:** *Robert De Niro*, *Tom Hanks*, *Al Pacino*

---

## 🔗 Correlation Insights

| Relationship             | Correlation | Insight                               | Recommendation              |
| ------------------------ | ----------- | ------------------------------------- | --------------------------- |
| **Gross vs IMDb Rating** | ~0.10       | Weak link between ratings and revenue | Focus on marketing & timing |
| **Gross vs Runtime**     | ~0.13       | Length doesn’t determine profit       | Prioritize story quality    |
| **Gross vs Year**        | ↑ over time | Profits rise post-2000                | Invest in global releases   |
| **IMDb vs Meta Score**   | ~0.27       | Critics & audiences mostly agree      | Balance both appeals        |
| **Votes vs Gross**       | ~0.57       | Popularity drives earnings            | Expand global distribution  |
| **Votes vs IMDb**        | ~0.48       | Higher ratings attract more votes     | Promote high-rated titles   |
| **Meta Score vs Gross**  | ~0          | Critics ≠ Revenue                     | Balance art and commerce    |

---

## 🧠 Genre-Based Insights

| Metric                  | Top Genres                 | Interpretation              |
| ----------------------- | -------------------------- | --------------------------- |
| **Highest IMDb Rating** | War, Western, Film-Noir    | Critically acclaimed genres |
| **Highest Gross**       | Adventure, Action, Fantasy | Strongest commercial appeal |

---

## 📈 Trends Over Time

* **Average Gross** has increased significantly over years (global market growth).
* **Average IMDb Rating** remains relatively stable.
* **Directors with consistent high ratings** contribute strongly to movie success.

---

## 🌐 Streamlit Dashboard

A user-friendly dashboard was developed using **Streamlit** to interact with the dataset.

### Pages Included:

1. **App Page** – Overview and introduction
2. **Overview** _ Key insights and Distributions
3. **Certificates Analysis** – Filter and visualize movies by certificate
4. **Meta Score Analysis** – Explore distribution and average meta scores
5. **Directors Analysis** _ Explore top directors and show movies
6. **Stars Analysis** _ Explore top stars and rating Distribution for the star
7. **Runtime Analysis** _ Explore distribution of the runtime for movies
8. **Genres Analysis** _ Explore genres and top genres by number of movies
9. **Relationships** – Explore correlations (gross vs IMDb, runtime, meta score, etc.)

Run locally:

```bash
streamlit run Home.py
```

---

## 🎯 Key Takeaways

* High IMDb or Meta Scores don’t guarantee box office success.
* Franchise movies dominate revenue generation.
* Drama and Crime remain timeless genres.
* Popularity (number of votes) is a strong revenue indicator.
* Data-driven storytelling + marketing = higher commercial success.

---؟
