import pandas as pd

def clean_text(text: str) -> str:
   
    if pd.isna(text):
        return ""
    return text.lower().replace(",", " ").strip()


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean Netflix dataset for recommendation system.
    """
    df = df.copy()

    # Step 1: Keep relevant columns
    cols = ["Title", "Category", "Type", "Cast", "Director", "Description"]
    df = df[cols]

    # Step 2: Fill missing values only where needed
    for col in ["Cast", "Director"]:
        df[col] = df[col].fillna("")

    # Step 3: Clean titles for reliable matching
    df["Title"] = df["Title"].str.lower().str.strip()

    # Step 4: Clean text columns for similarity
    for col in ["Type", "Cast", "Director", "Description"]:
        df[col] = df[col].apply(clean_text)

    # Step 5: Combine all features into one column for TF-IDF
    df["combined_features"] = (
        df["Type"] + " " +
        df["Cast"] + " " +
        df["Director"] + " " +
        df["Description"]
    )

    return df