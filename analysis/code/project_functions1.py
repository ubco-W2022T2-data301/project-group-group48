import numpy as np
import pandas as pd

def load_and_process(data_file):
    # Load data into dataframe
    singsong = pd.read_csv(data_file)

    # Select relevant columns and rename them
    singsong_cleaned = (
        singsong[['song_name', 'genre', 'song_popularity', 'song_duration_ms', 'acousticness', 
                  'danceability', 'energy', 'key', 'loudness', 'speechiness', 'tempo', 'audio_valence']]
        .rename(columns={'song_name': 'Song Name', 'song_popularity': 'Popularity', 
                         'song_duration_ms': 'Duration (ms)', 'acousticness': 'Acousticness',
                          'danceability': 'Danceability', 'energy': 'Energy', 'key': 'Key',
                          'loudness': 'Loudness', 'speechiness': 'Speechiness', 'tempo': 'Tempo', 
                          'audio_valence': 'Valence'})
    )
    
    # Create combo dataframe using method chaining
    combo = (
        singsong_cleaned
        .sort_values('Popularity')
        .pipe(lambda df: pd.concat([
            df.head(20),  # Top 20 most popular songs
            df.tail(20),  # Bottom 20 least popular songs
            df.iloc[len(df) // 2 - 5:len(df) // 2 + 5]  # Middle 10 songs
        ]))
        .sort_values('Popularity')
    )

    # Drop duplicates and add genre column
    combo_2 = (
        combo
        .drop_duplicates()
        .assign(genre=['Latin Pop', 'Son cubano', 'Bolero', 'Hip Hop', 'Rock', 'R&B', 'Rock', 'Rock', 
                       'Rock', 'Rock', 'Rock', 'Rock', 'Rock', 'Rock', 'Rock', 'Rock', 'Salsa', 'Rock', 
                       'Pop', 'R&B', 'Rock', 'Rock', 'Indie', 'Rock', 'Rock', 'Rock', 'Rock', 'Rock', 
                       'Rock', 'Pop', 'Rock', 'Rock', 'Rock', 'Rock', 'Pop', 'Pop', 'Pop', 'Pop', 'R&B', 
                       'Pop', 'Reggae', 'Reggae', 'Hip Hop', 'Hip Hop', 'Pop', 'Pop', 'Hip Hop', 'Reggae'])
        .reindex(columns=['Song Name', 'genre', 'Popularity', 'Duration (ms)', 'Acousticness', 'Danceability', 
                          'Energy', 'Key', 'Loudness', 'Speechiness', 'Tempo', 'Valence'])
    )

    return combo_2