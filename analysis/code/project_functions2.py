import numpy as np
import pandas as pd

def get_new_most_popular(songs_cleaned, Genre):
return (songs_cleaned
.sort_values("song_popularity", ascending=False)
.head(25)
.drop(labels=[353, 126, 155], axis=0)
.assign(Genre=Genre))

new_most_popular = get_new_most_popular(songs_cleaned, Genre)
new_most_popular 