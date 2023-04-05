import numpy as np
import pandas as pd

def load_and_process(songdata):
    songdata = (
    pd.read_csv ("/Users/Annabellengarambe/Desktop/DATA_301/project-group-group48/data/raw/song_data.csv.zip") # Load data into dataframe
    .drop_duplicates(subset= 'song_name')# Drop duplicates in the dataset
    .loc [0:510] #Return only first 500 songs
    )   
  
    songdata_cleaned = (
        songdata.drop(['audio_mode', 'time_signature'],axis=1) #drop useless columns
        .dropna(axis=0)   #drop na values
                     
    )
        
   
    songdata_sorted = (
        songdata.sort_values(by='song_popularity', ascending=False).reset_index() #Sort songs by popularity in descending order
    )
    
    
    # This creates a new column that multiplies each loudness value to the corresponding energy value
    def multiply_columns(row):
        return row['energy'] * row['loudness']
    songdata_sorted['Loud_Enrgy_Prod'] = (songdata_sorted.aggregate(multiply_columns, axis=1)) 

    
    
    
    
## divide into top 15 and process top 15       
    songdata_top = (
        (songdata_sorted.head(20)
               .assign(genre=['Reggae', 'Hip Hop', 'Pop', 'Pop', 'Hip Hop', 'Pop', 'Hip Hop', 
                              'Reggae', 'Reggae', 'Pop', 'R&B', 'Pop',  'Pop', 'Pop', 'Rock', 
                              'Pop', 'Rock', 'R&B', 'Rock', 'Rock'])
               .reindex(columns=['song_name', 'genre', 'song_popularity', 'song_duration_ms', 
                                 'acousticness', 'danceability', 'energy','instrumentalness',
                                 'key', 'liveness','loudness', 'speechiness', 'tempo', 'audio_valence',
                                 'Loud_Enrgy_Prod'])
        )
    )

## divide into bottom and process bottom 15
    songdata_bottom = (
        songdata_sorted.tail(20).sort_values(by=['song_popularity'], ascending = True)\
        .assign(genre=['Latin Pop', 'Son cubano', 'Bolero', 'Hip Hop', 'Rock', 'R&B', 
                       'Rock', 'Rock', 'Rock', 'Rock', 'Rock', 'Rock', 'Rock', 'Rock', 
                       'Rock','Salsa', 'Rock', 'Pop', 'R&B', 'Rock'])\
        .reindex(columns=['song_name', 'genre', 'song_popularity', 'song_duration_ms', 
                          'acousticness', 'danceability', 'energy','instrumentalness',
                          'key', 'liveness','loudness', 'speechiness', 'tempo', 'audio_valence', 
                          'Loud_Enrgy_Prod'])
    )
    
    
    concatenated_df = pd.concat([songdata_top, songdata_bottom], ignore_index=True)
    
    return concatenated_df