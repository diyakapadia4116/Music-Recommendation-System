from sklearn.neighbors import NearestNeighbors

def recommend_songs(df, song_name, genre, top_n=10):

    # Filter by genre and drop duplicates so you get unique song recommendations
    genre_df = df[df["track_genre"] == genre].drop_duplicates(subset=["track_name", "artists"]).reset_index(drop=True)

    if genre_df.empty:
        return "No songs found in this genre."

    feature_columns = [
        "danceability",
        "energy",
        "loudness",
        "speechiness",
        "acousticness",
        "instrumentalness",
        "liveness",
        "valence",
        "tempo"
    ]

    # Fill any missing values with 0 to prevent the NearestNeighbors model from crashing
    genre_features = genre_df[feature_columns].fillna(0)

    model = NearestNeighbors(
        metric="cosine",
        algorithm="brute"
    )

    model.fit(genre_features)

    matches = genre_df[
        genre_df["track_name"].str.lower() == song_name.lower()
    ]

    if matches.empty:
        return f'"{song_name}" not found in {genre} genre.'

    song_index = matches.index[0]

    distances, indices = model.kneighbors(
        genre_features.iloc[[song_index]],
        n_neighbors=min(top_n + 1, len(genre_df))
    )

    recommendations = genre_df.iloc[
        indices.flatten()[1:]
    ][[
        "track_id",
        "track_name",
        "artists",
        "album_name",
        "track_genre",
        "popularity"
    ]]

    return recommendations