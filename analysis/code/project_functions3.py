import numpy as np
import pandas as pd

def clean_and_concat(songdata):
    songdata_cleaned = (
    pd.read_csv("../../data/raw/song_data.csv.zip")
    .loc[1000:1510]
    .drop(['audio_mode', 'time_signature'], axis=1)
    .dropna(axis=0)
    .drop_duplicates(subset='song_name')
    .sort_values(by='song_popularity', ascending=False)
    .reset_index()
    .assign(Loud_Enrgy_Prod = lambda x: x['energy'] * x['loudness'])
    .assign(Vale_Dance_Prod = lambda x: x['audio_valence'] * x['danceability'])
)
    
    concatenated_df = (
        songdata_cleaned
        .head(50)
        .assign(genre=['Trap', 'Pop Rock', 'Trap', 'Hip Hop', 'Hip Hop', 'Pop', 'Pop Rock', 'Trap', 'Hip Hop', 'Trap', 'Hip Hop', 'Hip Hop', 'Hip Hop', 'Hip Hop', 'Trap', 'Pop', 'Trap', 'Hip Hop', 'Trap', 'Trap', 'Hip Hop', 'Trap', 'Hip Hop', 'Indie', 'Pop Rock', 'Pop', 'Hip Hop', 'Pop', 'Electronic', 'Acoustic Pop', 'Pop', 'Hip Hop', 'Alternative Rock', 'Pop', 'Hip Hop', 'Alternative Rock', 'Rock', 'Hip Hop', 'Pop Rock', 'Pop', 'Pop', 'Hip Hop', 'Trap', 'Pop Rock', 'Grunge', 'Hip Hop', 'Hip Hop', 'Pop', 'Alternative Rock', 'Pop Rock'])
        .reindex(columns=['song_name', 'genre', 'song_popularity', 'song_duration_ms', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'key', 'liveness', 'loudness', 'speechiness', 'tempo', 'audio_valence', 'Loud_Enrgy_Prod', 'Vale_Dance_Prod'])
        .append(
            songdata_cleaned
            .tail(50)
            .sort_values(by=['song_popularity'], ascending=True)
            .assign(genre=['Alternative Rock', 'Hip Hop', 'Bolero', 'Latin Pop', 'Latin Pop', 'Alternative Rock', 'Bolero', 'Alternative Rock', 'Latin Pop', 'Bolero', 'Alternative Rock', 'Bolero', 'Bolero', 'Rock', 'Alternative Rock', 'Alternative Rock', 'Bolero', 'Norteño', 'Alternative Rock', 'Rock', 'Alternative Rock', 'Latin Pop', 'Rock', 'Alternative Rock', 'Pop', 'Electronic', 'Hip Hop', 'Latin Pop', 'Bachata', 'Alternative Rock', 'Pop', 'Pop', 'Norteño', 'Grunge', 'Acoustic Pop', 'Gospel', 'Bolero', 'Pop', 'Indie', 'Alternative Rock', 'Alternative Rock', 'Reggae', 'Pop', 'Indie', 'Pop', 'R&B', 'Pop Rock', 'Indie', 'Pop', 'Pop'])
            .reindex(columns=['song_name', 'genre', 'song_popularity', 'song_duration_ms', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'key', 'liveness', 'loudness', 'speechiness', 'tempo', 'audio_valence', 'Loud_Enrgy_Prod', 'Vale_Dance_Prod'])
        )
    ) 
    return concatenated_df
