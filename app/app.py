import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from utils import recommend_songs

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="Spotify Music Recommender",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------
# Load CSS
# ---------------------------------------------------
try:
    with open("app/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("Could not find style.css. Ensure the path is correct.")

# ---------------------------------------------------
# Load Dataset
# ---------------------------------------------------
@st.cache_data
def load_dataset():
    from pathlib import Path
    BASE_DIR = Path(__file__).resolve().parent.parent
    DATASET_PATH = BASE_DIR / "models" / "music_dataset.csv"
    return pd.read_csv(DATASET_PATH)

df = load_dataset()

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------
with st.sidebar:
    st.markdown("# 🎵 Spotify Recommender")
    st.write("---")
    st.markdown(
        """
        A Content-Based Music Recommendation System built using:
        - Nearest Neighbors
        - Cosine Similarity
        - Streamlit
        - Scikit-Learn
        """
    )
    st.write("---")
    st.metric("Songs Indexed", f"{len(df):,}")
    st.metric("Genres Available", df["track_genre"].nunique())
    st.write("---")
    st.caption("Developed by Diya Kapadia ❤️")

# ---------------------------------------------------
# Hero Section
# ---------------------------------------------------
st.markdown(
    """
<div class='hero'>
    <h1>🎵 Music Recommendation Engine</h1>
    <p>Discover new tracks based on audio similarity, genre, and musical characteristics.</p>
</div>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------
# Main Layout Columns
# ---------------------------------------------------
left, right = st.columns([1, 2.5], gap="large")

# ===================================================
# LEFT PANEL: FILTERS
# ===================================================
with left:
    st.markdown("### 🎼 Tune Your Search")
    
    genres = sorted(df["track_genre"].dropna().unique())
    genre = st.selectbox("Choose Genre", genres)
    
    # Filter songs by genre and drop NaN values to prevent sorting errors
    songs = sorted(df[df["track_genre"] == genre]["track_name"].dropna().unique())
    song = st.selectbox("Choose Song", songs)
    
    top_n = st.slider("Number of Recommendations", min_value=5, max_value=20, value=10, step=1)
    
    st.write("") 
    recommend = st.button("🎧 Recommend Songs", use_container_width=True)

# ===================================================
# RIGHT PANEL: RECOMMENDATIONS
# ===================================================
with right:
    st.markdown("### 🎶 Recommended For You")

    if not recommend:
        st.info("👈 Select a genre and a track you love, then hit **Recommend Songs** to generate your playlist.")

    if recommend:
        with st.spinner("Analyzing audio features... 🎵"):
            try:
                recommendations = recommend_songs(
                    df=df,
                    song_name=song,
                    genre=genre,
                    top_n=top_n
                )

                if isinstance(recommendations, str):
                    st.error(recommendations)
                elif recommendations.empty:
                    st.warning("No recommendations found. Try a different track!")
                else:
                    # Dynamically create columns inside the right panel (2 per row)
                    cols = st.columns(2)
                    
                    for i, (_, row) in enumerate(recommendations.iterrows()):
                        
                        # Extract the unique Spotify track ID from the dataset
                        track_id = row['track_id']
                        
                        # Spotify's official embed iframe
                        spotify_player = f"""
<iframe style="border-radius:12px" 
src="https://open.spotify.com/embed/track/{track_id}?utm_source=generator&theme=0" 
width="100%" 
height="152" 
frameBorder="0" 
allowfullscreen="" 
allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" 
loading="lazy">
</iframe>
"""

                        # Zero indentation for EVERY line in the HTML card
                        card = f"""
<div class="song-card">
<h3>🎵 {row['track_name']}</h3>
<p>👤 <b>Artist:</b> {row['artists']}</p>
<p>🎼 <b>Genre:</b> {row['track_genre']}</p>
<div style="margin-top: 15px;">
{spotify_player}
</div>
</div>
"""
                        # Alternate between the two columns
                        with cols[i % 2]:
                            st.markdown(card, unsafe_allow_html=True)

            except Exception as e:
                st.error(f"Something went wrong while generating recommendations.\n\n{e}")

# Footer
st.markdown("---")
st.markdown(
    """
<div style="text-align:center; color:#b3b3b3; font-size: 0.9rem;">
    Built with ❤️ using <b>Python • Streamlit • Scikit-Learn</b><br><br>
    © 2026 Diya Kapadia
</div>
    """,
    unsafe_allow_html=True
)