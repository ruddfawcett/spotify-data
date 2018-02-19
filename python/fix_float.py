import pandas as pd
data = pd.read_csv('billboard_spotify_matched_data.csv')
data.to_csv('billboard_spotify_matched_data.csv', float_format='%.6f')
