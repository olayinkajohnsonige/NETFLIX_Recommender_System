# Netflix Content-Based Recommender System

A content-based recommendation engine that suggests similar Netflix movies and TV shows using metadata such as genre, cast, director, and description.

---

## 🔗 Live Demo


---[Netflix Recommender System]()

## Overview

This project implements a recommendation engine designed to help users discover Netflix content based on content similarity. Rather than relying on user ratings or collaborative filtering, the system leverages **metadata-driven analysis** to identify relationships between titles.

The system transforms movie and show attributes into numerical representations using TF-IDF vectorization and computes similarity using cosine distance metrics to generate meaningful recommendations.

---

## Features

- **Content-based recommendations** using:
  - Genre classification
  - Cast information
  - Director details
  - Content description
- **TF-IDF vectorization** for intelligent text feature extraction
- **Cosine similarity** computation for accurate content matching
- **Interactive user interface** built with Streamlit
- **Filtering capabilities** by content type (Movie/TV Show)
- **Error handling** for missing or invalid titles
- **Optimized performance** with model caching

---

## How It Works

### 1. Data Preprocessing

The system begins by extracting and cleaning relevant columns from the Netflix dataset:

- Text normalization (lowercasing, punctuation removal)
- Missing value handling
- Feature consolidation into unified text representation

```text
combined_features = Type + Cast + Director + Description
```

### 2. TF-IDF Vectorization

Each title is converted into a numerical vector using TF-IDF (Term Frequency-Inverse Document Frequency):

- Words that are **frequent in a specific title but rare across the dataset** receive higher importance scores
- Common words are automatically downweighted to reduce noise

### 3. Cosine Similarity Computation

The system calculates similarity between all titles:

```text
similarity(title_A, title_B) → value between 0 and 1
```

- **1.0** = highly similar content
- **0.0** = dissimilar content

### 4. Recommendation Engine

Given a user-selected title:

1. Locate the title in the dataset
2. Retrieve similarity scores against all other titles
3. Sort by descending similarity
4. Apply content-type filtering (optional)
5. Return top-N recommendations

---

## Project Structure

```
netflix-recommender/
│
├── data/
│   └── netflix_titles.csv          # Dataset source
│
├── src/
│   ├── data_loader.py              # Dataset loading utilities
│   ├── preprocessing.py            # Data cleaning and preparation
│   └── recommender.py              # TF-IDF + similarity logic
│
├── app/
│   └── app.py                      # Streamlit application
│
├── requirements.txt                # Python dependencies
└── README.md                       # Documentation
```

---

## Quick Start

### Prerequisites

- Python 3.7+
- pip

### Installation

```bash
git clone https://github.com/olayinkajohnsonige/NETFLIX_Recommender_System
cd NETFLIX_Recommender_System

pip install -r requirements.txt
```

### Running the Application

```bash
streamlit run app/app.py
```

Access the application at:

```
http://localhost:8501
```

---

## Usage Example

**Input:**
```
The 100
```

**Output:**
- Star Trek: Deep Space Nine
- Lost in Space
- The Umbrella Academy
- The Vampire Diaries

---

## Technical Stack

| Component | Technology |
|-----------|-----------|
| Language | Python 3.7+ |
| Data Processing | Pandas, NumPy |
| ML/Similarity | scikit-learn |
| User Interface | Streamlit |

---

## Known Limitations

- **No personalization**: Returns identical recommendations for all users with the same input
- **Metadata-dependent**: Relies on dataset quality and completeness
- **Text-based matching**: May not capture abstract or thematic similarities
- **No temporal factors**: Does not consider trends or release dates
- **Dataset scope**: Limited to Netflix titles in the source dataset

---

## Future Enhancements

- Integration with TMDB API for movie posters and additional metadata
- Display similarity scores and reasoning for recommendations
- Hybrid recommendation system combining content and collaborative filtering
- Public deployment for broader accessibility
- Performance optimization for larger datasets
- User rating integration for improved accuracy

---

## Performance Considerations

- Model trained and cached for rapid inference
- O(n) lookup time for individual recommendations
- Scalable to 10,000+ titles with standard hardware
- Streamlit caching reduces redundant computations

---

## Troubleshooting

**Title Not Found:**
- Verify exact spelling and capitalization
- Check if title exists in the dataset
- Try filtering by content type

**Slow Performance:**
- Ensure Python virtual environment is active
- Clear Streamlit cache: `streamlit cache clear`
- Verify sufficient system memory (2GB+ recommended)

---

## Contributing

Contributions are welcome. Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -m 'Add feature'`)
4. Push to branch (`git push origin feature/improvement`)
5. Open a Pull Request

---

## License

This project is licensed under the MIT License. See LICENSE file for details.

---

## Author

**Olayinka Johnson-Ige**

---

## Last Updated

March 2026

---

## Support

For issues, questions, or suggestions, please open an issue on the repository or contact the author.

---

