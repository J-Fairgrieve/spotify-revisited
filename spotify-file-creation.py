# Import relevant libraries
print("Importing libraries & credentials...")
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Import spotify credentials
from spotify_creds import cid
from spotify_creds import secret

# Load Spotify credentials
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)



# Save the playlist codes as variables
print("Saving playlist codes...")
top_50 = "37i9dQZEVXbLnolsZ8PSNw?si=8578340d8d9d4179"
viral_50 = "37i9dQZEVXbL3DLHfQeDmV?si=dbc713206df743d2"



# Create the blank list data
print("Creating dataframes for the UK top 50 playlist...")
artist_name = []
track_name = []
popularity = []
track_id = []
album_id = []
release_date = []
markets = []
album_name = []
followers = []
genres = []

# Run a loop for the top 50 playlist
track_results = sp.playlist(top_50)
for i, t in enumerate(track_results['tracks']["items"]):
    artist_name.append(t["track"]["artists"][0]["name"])
    track_name.append(t["track"]["name"])
    track_id.append(t["track"]["id"])
    popularity.append(t["track"]["popularity"])
    album_id.append(t["track"]["album"]["id"])
    genres.append(sp.artist(t["track"]["artists"][0]["id"])["genres"])
    release_date.append(t["track"]["album"]["release_date"])
    markets.append(t["track"]["album"]["available_markets"])
    album_name.append(t["track"]["album"]["name"])
    followers.append(sp.artist(t["track"]["artists"][0]["id"])["followers"]["total"])

# Create a dataframe for the top 50 data
top_50_df = pd.DataFrame({"artist_name" : artist_name,
                         "artist_genres" : genres,
                         "album_id" : album_id,
                         "album_name" : album_name,
                         'track_id' : track_id,
                         'track_name' : track_name,
                         'popularity' : popularity,
                         "release_date" : release_date,
                         "markets" : markets,
                         "followers" : followers})

# Create the list of track features
features = []

for x in track_id:
    features.append(sp.audio_features(x))
    
# Create the DataFrame for track features
feat_top_df = pd.DataFrame()

for i in range(len(features)):
    feat_top_df = feat_top_df.append(features[i][0], ignore_index=True)
    
# Rename track id column for future merging with the other DataFrame
feat_top_df.rename(columns = {'id':'track_id'}, inplace = True)

# Merge the two DataFrames together & remove any duplicate tracks to get final data file
top_50_data = top_50_df.merge(feat_top_df, how = "outer", on = "track_id")



# Create the blank list data
print("Creating dataframes for the UK viral 50 playlist...")
artist_name = []
track_name = []
popularity = []
track_id = []
album_id = []
release_date = []
markets = []
album_name = []
followers = []
genres = []

# Run a loop for the viral 50 playlist
track_results = sp.playlist(viral_50)
for i, t in enumerate(track_results['tracks']["items"]):
    artist_name.append(t["track"]["artists"][0]["name"])
    track_name.append(t["track"]["name"])
    track_id.append(t["track"]["id"])
    popularity.append(t["track"]["popularity"])
    album_id.append(t["track"]["album"]["id"])
    genres.append(sp.artist(t["track"]["artists"][0]["id"])["genres"])
    release_date.append(t["track"]["album"]["release_date"])
    markets.append(t["track"]["album"]["available_markets"])
    album_name.append(t["track"]["album"]["name"])
    followers.append(sp.artist(t["track"]["artists"][0]["id"])["followers"]["total"])

# Create a dataframe for the top 50 data
viral_50_df = pd.DataFrame({"artist_name" : artist_name,
                         "artist_genres" : genres,
                         "album_id" : album_id,
                         "album_name" : album_name,
                         'track_id' : track_id,
                         'track_name' : track_name,
                         'popularity' : popularity,
                         "release_date" : release_date,
                         "markets" : markets,
                         "followers" : followers})

# Create the list of track features
features = []

for x in track_id:
    features.append(sp.audio_features(x))
    
# Create the DataFrame for track features
feat_viral_df = pd.DataFrame()

for i in range(len(features)):
    feat_viral_df = feat_viral_df.append(features[i][0],ignore_index=True)
    
# Rename track id column for future merging with the other DataFrame
feat_viral_df.rename(columns = {'id':'track_id'}, inplace = True)

# Merge the two DataFrames together & remove any duplicate tracks to get final data file
viral_50_data = viral_50_df.merge(feat_viral_df, how = "outer", on = "track_id")



# export the final created data files
print("Saving csv files...")
viral_50_data.to_csv("Resources/Viral 50 Data.csv", index = False)
top_50_data.to_csv("Resources/Top 50 Data.csv", index = False)
print("...Script complete, enjoy!")