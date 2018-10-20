from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import json
import requests
import pandas as pd
from get_data import *

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace=False

df = pd.read_csv("test.csv")

maxDance = df['danceability'].max()
targetDance = df['danceability'].mean()
minDance = df['danceability'].min()

maxEnergy = df['energy'].max()
targetEnergy = df['energy'].mean()
minEnergy = df['energy'].min()

maxAcoustic = df['acousticness'].max()
targetAcoustic = df['acousticness'].mean()
minAcoustic = df['acousticness'].min()

maxInstrument = df['instrumentalness'].max()
targetInstrument = df['instrumentalness'].mean()
minInstrument = df['acousticness'].min()

maxLive = df['liveness'].max()
targetLive = df['liveness'].mean()
minLive = df['liveness'].min()

maxLoud = df['loudness'].max()
targetLoud = df['loudness'].mean()
minLoud = df['loudness'].min()

maxSpeech = df['speechiness'].max()
targetSpeech = df['speechiness'].mean()
minSpeech = df['speechiness'].min()

maxTempo = df['tempo'].max()
targetTempo = df['tempo'].mean()
minTempo = df['tempo'].min()

maxValence = df['valence'].max()
targetValence = df['valence'].mean()
minValence = df['valence'].min()

seedGenres = df['artist genres']
seedArtists = df['artist']

test_list = []
test_list.append(str(targetDance.item()))
print(test_list)

#listOfRecs = sp.recommendations(seed_artists=seedArtists, seed_genres=seedGenres, seed_tracks=None, limit=5, country=None, min_acousticness=minAcoustic, max_acousticness=maxAcoustic, target_acousticness=targetAcoustic, min_danceability=minDance, max_danceability=maxDance, target_danceability=targetDance, min_energy=minEnergy, max_energy=maxEnergy, target_energy=targetEnergy, min_instrumentalness=minInstrument, max_instrumentalness=maxInstrument, target_instrumentalness=targetInstrument, min_liveness=minLive, max_liveness=maxLive, target_liveness=targetLive, min_loudness=minLoud, max_loudness=maxLoud, target_loudness=targetLoud, min_speechiness=minSpeech, max_speechiness=maxSpeech, target_speechiness=targetSpeech, min_tempo=minTempo, max_tempo=maxTempo, target_tempo=targetTempo, min_valence=minValence, max_valence=maxValence, target_valence=targetValence)
listOfRecs = sp.recommendations(seed_artists=['spotify:artist:70cRZdQywnSFp9pnc2WTCE'], target_danceability=test_list, limit=20)
print(get_track_names(listOfRecs['tracks']))
