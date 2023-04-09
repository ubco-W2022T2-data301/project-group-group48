import numpy as np
import pandas as pd

def load_and_process(data_file):
    # Load data into dataframe
    singsong = pd.read_csv(data_file)

    # drop irrelevant columns
    singsong_cleaned = (
        singsong.drop(['audio_mode','liveness', 'time_signature',], axis=1)
    )
    
    # Create combo dataframe using method chaining
    combo = (
        singsong_cleaned
        .sort_values('song_popularity')
        .pipe(lambda df: pd.concat([
            df.head(20),  # Top 20 most popular songs
            df.tail(20),  # Bottom 20 least popular songs
            df.iloc[len(df) // 2 - 5:len(df) // 2 + 5]  # Middle 10 songs
        ]))
        .sort_values('song_popularity')
    )

    # Drop duplicates and add genre column
    combo_2 = (
            combo
            .drop_duplicates()
            .assign(genre=['rock', 'rock', 'rock', 'rock', 'rock', 'rock', 'rock', 'rock', 'pop', 'pop', 'pop', 'rock', 'rock', 'rock', 'rock', 'rock', 'rock', 'pop', 'pop', 'metal', 'hip hop', 'pop', 'pop', 'post-punk', 'hip hop', 'grunge', 'hard rock', 'pop', 'rock', 'rock', 'rock', 'pop punk', 'hip hop', 'pop', 'hard rock', 'hip hop', 'hard rock', 'new wave', 'pop', 'pop', 'pop rock', 'soft rock'])
            .reindex(columns=['song_name', 'genre', 'song_popularity', 'song_duration_ms', 'acousticness', 'danceability', 'energy', 'key', 'loudness', 'speechiness', 'tempo', 'audio_valence', 'loudness_energy', 'energy_duration'])
    )
           

    return combo_2