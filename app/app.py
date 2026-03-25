import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.recommender import build_similarity_matrix, create_indices, recommend

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(page_title="Netflix Recommender", layout="wide")

# -------------------------
# CUSTOM STYLING (DARK THEME)
# -------------------------
st.markdown("""
    <style>
        body {
            background-color: #0b0f19;
        }
        .stTextInput input {
            background-color: #111827 !important;
            color: white !important;
        }
        .stSelectbox div {
            background-color: #111827 !important;
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

# -------------------------
# CACHED FUNCTIONS
# -------------------------
@st.cache_data(show_spinner=False)
def load_and_preprocess():
    df = load_data(r"C:\Users\lizzy\OneDrive\Desktop\ReposBackup\Project_1\data\raw\Netflix Dataset.csv")
    return preprocess_data(df)

@st.cache_resource(show_spinner=False)
def build_model(df_clean):
    cosine_sim = build_similarity_matrix(df_clean)
    indices = create_indices(df_clean)
    return cosine_sim, indices

df_clean = load_and_preprocess()
cosine_sim, indices = build_model(df_clean)

# -------------------------
# UI HEADER
# -------------------------
st.title("🎬 Netflix Recommender System")
st.markdown("Find movies and shows similar to what you love 🍿")

# -------------------------
# INPUT SECTION (COLUMNS)
# -------------------------
col1, col2 = st.columns(2)

with col1:
    movie_title = st.text_input("Enter a movie title:")

with col2:
    category = st.selectbox("Filter by type:", ["All", "Movie", "TV Show"])

# -------------------------
# BUTTON ACTION
# -------------------------
if st.button("🎯 Get Recommendations"):
    if movie_title:
        selected_category = None if category == "All" else category

        results = recommend(
            movie_title,
            df_clean,
            cosine_sim,
            indices,
            top_n=10,
            category=selected_category
        )

        st.subheader("🎥 Recommendations")

        # -------------------------
        # HANDLE ERROR MESSAGE
        # -------------------------
        if isinstance(results, str):
            st.warning(results)

        else:
            # 🔥 Get full rows instead of just titles
            result_df = df_clean[df_clean["Title"].isin(results)]

            cols = st.columns(2)

            for i, (_, row) in enumerate(result_df.iterrows()):
                with cols[i % 2]:
                    st.markdown(f"""
                    <div style="
                        padding:15px;
                        border-radius:12px;
                        background-color:#1f2937;
                        margin-bottom:15px;
                        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
                    ">
                        <h3 style="color:white;">{row['Title'].title()}</h3>
                        <p style="color:#9ca3af;"><b>Type:</b> {row['Category']}</p>
                        <p style="color:#d1d5db;">
                            {row['Description'][:150]}...
                        </p>
                    </div>
                    """, unsafe_allow_html=True)

    else:
        st.warning("Please enter a movie title.")