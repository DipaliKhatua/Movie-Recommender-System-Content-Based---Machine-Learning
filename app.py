import streamlit as st
import pickle
import requests

# Function to fetch movie posters from TMDB API
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path', '')  # Avoid errors if poster_path is missing
    return f"https://image.tmdb.org/t/p/w500/{poster_path}" if poster_path else ""

# Recommendation function
def recommend(movie):
    index = list(movies_df['title']).index(movie)  # Use movies_df to find index
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:  # Get top 5 similar movies
        movie_id = movies_df.iloc[i[0]].movie_id  # Get movie_id from DataFrame
        recommended_movie_names.append(movies_df.iloc[i[0]].title)  # Get title
        recommended_movie_posters.append(fetch_poster(movie_id))  # Fetch poster

    return recommended_movie_names, recommended_movie_posters

# Load data
movies_df = pickle.load(open('Artifacts/movies.pkl', 'rb'))  # Keep full dataset
similarity = pickle.load(open('Artifacts/similarity.pkl', 'rb'))  # Load similarity matrix
movies_list = movies_df['title'].values  # Extract only movie titles as NumPy array

# Streamlit UI
st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    'Select or Type Movie Name Here',
    movies_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)  # Use latest Streamlit columns method

    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])