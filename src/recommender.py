from sklearn.feature_extraction.text import TfidfVectorizer
from src.preprocessing import preprocess_data

def build_similarity_matrix(df):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df["combined_features"])
    
    from sklearn.metrics.pairwise import cosine_similarity
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
    return cosine_sim

def create_indices(df):
    import pandas as pd
    return pd.Series(df.index, index=df['Title']).drop_duplicates()

def recommend(title, df, cosine_sim, indices, top_n=10, category=None):
    title = title.lower().strip()

    # Check if title exists
    if title not in indices:
        return f"'{title}' not found "

    idx = indices[title]

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # remove itself
    sim_scores = sim_scores[1:]

    movie_indices = []

    for i, score in sim_scores:
        if category:
            if df.iloc[i]["Category"].lower() != category.lower():
                continue
        
        movie_indices.append(i)

        if len(movie_indices) == top_n:
            break

    if len(movie_indices) == 0:
        return "No recommendations found."

    return df["Title"].iloc[movie_indices].tolist()