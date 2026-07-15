# 🎵 Spotify Music Recommender

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)]([https://your-app-url.streamlit.app](https://music-recommendation-system-dk.streamlit.app/)

A **Content-Based Music Recommendation System** that helps users discover new tracks based on audio similarity, genre, and musical characteristics. Give the engine a track you love, and it will analyze its acoustic features to generate a curated playlist of similar songs.

---

## ✨ Features

* **Machine Learning Engine:** Uses K-Nearest Neighbors (KNN) and Cosine Similarity to find mathematically similar songs based on 9 distinct audio features (danceability, energy, tempo, etc.).
* **Interactive UI:** Built with Streamlit for a clean, responsive, and user-friendly web interface.
* **Live Previews:** Integrates the official Spotify Embed Player so you can listen to your recommendations directly in the browser.
* **Customizable Search:** Filter by genre and dynamically choose how many songs you want recommended.

---

## 🛠️ Tech Stack

* **Language:** Python
* **Frontend:** Streamlit
* **Machine Learning:** Scikit-Learn
* **Data Manipulation:** Pandas
* **Deployment:** Streamlit Community Cloud

---

## 🚀 How to Run Locally

Want to run this project on your own machine? Follow these steps:

**1. Clone the repository**
```bash
git clone [https://github.com/your-username/spotify-recommender.git](https://github.com/your-username/spotify-recommender.git)
cd spotify-recommender
```

**2. Install the required dependencies**
Make sure you have Python installed, then run:
```bash
pip install -r requirements.txt
```

**3. Run the Streamlit app**
```bash
streamlit run app.py
```
---

## 📂 Project Structure

The Music Recommendation System follows a modular project structure to keep the code organized, maintainable, and deployment-ready.

```text
spotify-recommender/
│
├── app.py                 # Main Streamlit application
├── utils.py               # Recommendation engine and ML logic
├── requirements.txt       # Project dependencies
│
├── app/
│   └── style.css          # Custom CSS for the Streamlit UI
│
└── models/
    └── music_dataset.csv  # Processed Spotify music dataset
```

---

## 💡 How It Works

* The dataset contains thousands of Spotify tracks, each scored on various acoustic features.

* When a user selects a song, the app isolates that song's exact feature array (e.g., high energy, low acousticness).

* The NearestNeighbors algorithm calculates the multi-dimensional distance between the chosen song and all other songs in that genre.

* The algorithm returns the songs with the shortest "distance" (highest similarity) to the target track.

--- 

## 👤 Author

Diya Kapadia

GitHub: @diyakapadia4116

LinkedIn: https://www.linkedin.com/in/diya-kapadia-3b7ba2317/
