
## What is a Recommender System?
A recommender system is an AI-driven tool that suggests relevant items (movies, products, music, etc.) to users based on their preferences, behavior, or content similarity. It helps users discover new items efficiently.

    ### Types of Recommender Systems:
        1. - Content-Based Filtering: Recommends items similar to those the user has liked, using features like keywords, metadata, or embeddings.
        - Example: If a user watches sci-fi movies on YouTube, the system recommends other sci-fi films based on genre and descriptions.
        2. - Collaborative Filtering: Suggests items based on user behavior and preferences, leveraging patterns from other users.
        - Example: If users with similar viewing habits like a particular movie, the system recommends it to others with similar tastes.
        3. - Hybrid Filtering: Combines content-based and collaborative filtering for more accurate recommendations.
        - Example: Netflix uses hybrid filtering—recommending shows based on both content similarity and user preferences.
        Since you're working with YouTube videos, content-based filtering will rely on video metadata, tags, transcripts, and descriptions for recommendations. Let me know if you need guidance on implementation!

Dataset Link: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

Movie Recommender System (Content-Based Filtering)
A machine learning-based Movie Recommendation System that suggests similar movies using cosine similarity on content features such as genres, keywords, cast, and overview.
Overview
This project builds a content-based filtering recommender system, using natural language processing (NLP) techniques. The system analyzes movie metadata and recommends similar movies based on text-based features.
Key Features
✅ Content-Based Filtering – Uses metadata (genres, keywords, overview, cast) for recommendations.
✅ TF-IDF & Cosine Similarity – Computes movie similarity based on textual descriptions.
✅ Streamlit UI – Provides an interactive web-based interface for users to select a movie and view recommendations.
✅ TMDB API Integration – Fetches movie posters dynamically.

Tech Stack
- Python – Core programming language
- Pandas, NumPy – Data preprocessing
- Scikit-Learn – Text vectorization (CountVectorizer), cosine similarity
- NLTK – Stemming for text normalization
- Streamlit – UI for displaying recommendations
- TMDB API – Fetching movie posters
- Pickle – Saving and loading models

Dataset Used
- movies.csv – Contains movie metadata (title, genres, overview, cast, crew, etc.).
- credits.csv – Provides cast and crew details.

Implementation Steps
1. Data Loading & Preprocessing
- Read movies.csv and credits.csv.
- Merge datasets using the 'title' column.
- Select relevant features (movie_id, title, overview, genres, keywords, cast, crew).
- Handle missing values and remove duplicates.
2. Feature Engineering
- Convert string-based lists (genres, keywords, cast, crew) into proper Python lists.
- Extract director information from the crew column.
- Tokenize and clean movie overview.
- Remove spaces in genres, keywords, cast, and crew names for better processing.
3. Text Vectorization
- Combine all metadata into a single "tags" column.
- Convert text data into a numerical representation using CountVectorizer.
- Apply stemming to normalize word forms.
4. Computing Similarities
- Use cosine similarity to find movies with similar content.
- Create a function to recommend top 5 movies based on similarity scores.
5. Building Streamlit UI
- Allow users to select a movie via Streamlit dropdown.
- Fetch and display recommended movies and their posters using the TMDB API.

How to Run Locally
Prerequisites
Ensure Python 3.7+ is installed.
Steps
- Clone the repository:
git clone [<repo-link>](https://github.com/DipaliKhatua/Movie-Recommender-System-Content-Based---Machine-Learning)
cd movie-recommender
- Install dependencies:
pip install -r requirements.txt
- Run the application:
streamlit run app.py
- Interact with the UI:
- Select a movie.
- Click “Show Recommendation” to view similar movies along with posters.

Future Enhancements
📌 Integrate collaborative filtering for better recommendations.
📌 Add user-based preferences for personalization.
📌 Improve metadata extraction using transformers-based NLP models.
