# 🎬 Content-Based Movie Recommendation System

A **Content-Based Movie Recommendation System** built with Python, scikit-learn, and Streamlit.  
This project recommends movies similar to your favorite picks based on their plot descriptions, with an interactive interface to display posters and plots using the OMDb API.

---

## 🛠️ Features

- **Text-Based Recommendations:** Uses `TfidfVectorizer` to extract features from movie descriptions.
- **Similarity Scoring:** Computes similarity between movies using `cosine_similarity`.
- **Interactive UI:** Built with **Streamlit** for a user-friendly experience.
- **Movie Details Fetching:** Integrates **OMDb API** to show movie posters and full plots alongside recommendations.

---

## 💡 How it Works

1. Enter the name of a movie you like.
2. The system finds movies with similar plots using cosine similarity.
3. Top recommendations are displayed with their poster and full plot.

---

## 🧰 Tech Stack

- Python  
- scikit-learn  
- Streamlit  
- Requests (for OMDb API)  
- Pickle (for saving preprocessed data)  



