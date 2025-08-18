import pickle
import streamlit as st
import requests
import os


def fetch_poster_omdb(movie_title):
    """Fetch movie poster URL using OMDb API."""
    api_key = "532b8c32"
    try:
        url = f"http://www.omdbapi.com/?t={movie_title}&apikey={api_key}"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        poster_url = data.get("Poster")
        return poster_url if poster_url and poster_url != "N/A" else None
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching poster: {e}")
        return None


@st.cache_resource
def load_pickle_from_gdrive(file_id, filename):
    """
    Download and load pickle file from Google Drive.
    """
    url = f"https://drive.google.com/uc?id={file_id}"
    if not os.path.exists(filename):
        response = requests.get(url)
        with open(filename, "wb") as f:
            f.write(response.content)
    with open(filename, "rb") as f:
        return pickle.load(f)


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),
                       reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_name = movies.iloc[i[0]].title
        recommended_movie_posters.append(fetch_poster_omdb(movie_name))
        recommended_movie_names.append(movie_name)
    return recommended_movie_names, recommended_movie_posters


# ---------------- Streamlit App ----------------
st.header('🎬 Movie Recommender System')

# Replace these with your actual Google Drive file IDs
MOVIE_LIST_FILE_ID = "1k-34RBAFewoIEQmrkXHg-pyrtdn8JW-J"
SIMILARITY_FILE_ID = "1yt_0AJyHWeJbIPftisSUTDC54EVGSxJR"

movies = load_pickle_from_gdrive(MOVIE_LIST_FILE_ID, "movie_list.pkl")
similarity = load_pickle_from_gdrive(SIMILARITY_FILE_ID, "similarity.pkl")

movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie:", movie_list)

if st.button('Show Recommendation'):
    names, posters = recommend(selected_movie)
    cols = st.columns(5)
    for col, name, poster in zip(cols, names, posters):
        with col:
            st.image(poster)
            st.text(name)
