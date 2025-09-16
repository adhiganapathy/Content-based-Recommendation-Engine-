import streamlit as st
import pickle
import requests

# -------------------------------
# Function to fetch movie details from OMDb
# -------------------------------
def get_movie_details(title, api_key):
    url = f"http://www.omdbapi.com/?t={title}&plot=full&apikey={api_key}"
    res = requests.get(url).json()
    if res.get("Response") == "True":
        plot = res.get("Plot", "N/A")
        poster = res.get("Poster", "N/A")
        return plot, poster
    return "N/A", "N/A"

# -------------------------------
# Load preprocessed data
# -------------------------------
movies = pickle.load(open(
    r"C:\Users\Adhi Ganapathy\Documents\Python_ws\Recommendation Engine 13092025\Model\Recommender.pkl", "rb"
))
similarity = pickle.load(open(
    r"C:\Users\Adhi Ganapathy\Documents\Python_ws\Recommendation Engine 13092025\Model\similarity.pkl", "rb"
))

# -------------------------------
# Recommender Function
# -------------------------------
def recommend_movies(movie_name, top_n=5):
    if movie_name.lower() not in movies['title'].str.lower().values:
        return []

    # Find the index of the movie
    idx = movies[movies['title'].str.lower() == movie_name.lower()].index[0]

    # Get similarity scores
    sim_scores = list(enumerate(similarity[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:top_n+1]

    # Get recommended movie titles
    movie_indices = [i[0] for i in sim_scores]
    return movies.iloc[movie_indices]['title'].tolist()

# -------------------------------
# Streamlit UI
# -------------------------------
API_KEY = "745ed997"  # just the key, not the full URL

st.title("🎬 Movie Recommendation System")

movie = st.text_input("Enter a movie name (Hollywood works best):")

if st.button("Recommend"):
    recommendations = recommend_movies(movie)
    if not recommendations:
        st.error("No recommendations found! Please try another movie.")
    else:
        for title in recommendations:
            plot, poster = get_movie_details(title, API_KEY)
            st.subheader(title)
            if poster == "N/A":
                st.write(plot)
                
            else:
                col1,col2 = st.columns([1,2])
                with col1:
                    st.image(poster, width=200)
                with col2:
                    st.write(plot)
                
            st.markdown("---")