import pickle
import streamlit as st
import requests


def fetch_poster_omdb(movie_title):
    """
    Fetch movie poster URL using OMDb API.

    Parameters:
        movie_title (str): Name of the movie
        

    Returns:
        str: Poster URL if found, else None
    """
    api_key="532b8c32"
    try:
        url = f"http://www.omdbapi.com/?t={movie_title}&apikey={api_key}"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        # OMDb returns 'Poster' field directly
        poster_url = data.get("Poster")

        if poster_url and poster_url != "N/A":
            return poster_url
        else:
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster from OMDb: {e}")
        return None



def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_name = movies.iloc[i[0]].title
        recommended_movie_posters.append(fetch_poster_omdb(movie_name))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


st.header('Movie Recommender System')
movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(recommended_movie_posters[0])
        st.text(recommended_movie_names[0])
    with col2:
        st.image(recommended_movie_posters[1])
        st.text(recommended_movie_names[1])

    with col3:
        st.image(recommended_movie_posters[2])
        st.text(recommended_movie_names[2])
    with col4:
        st.image(recommended_movie_posters[3])
        st.text(recommended_movie_names[3])
    with col5:
        st.image(recommended_movie_posters[4])
        st.text(recommended_movie_names[4])




