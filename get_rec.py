from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import json
import requests
import pandas as pd
import ast
from get_data import *
from collections import Counter

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace=False

df = pd.read_csv("test.csv")

#read from spreadsheet to determine the common the max, min, and average (target) for each attribute in the playlist
maxDance = [df['danceability'].max()]
targetDance = [df['danceability'].mean()]
minDance = [df['danceability'].min()]

maxEnergy = [df['energy'].max()]
targetEnergy = [df['energy'].mean()]
minEnergy = [df['energy'].min()]

maxAcoustic = [df['acousticness'].max()]
targetAcoustic = [df['acousticness'].mean()]
minAcoustic = [df['acousticness'].min()]

maxInstrument = [df['instrumentalness'].max()]
targetInstrument = [df['instrumentalness'].mean()]
minInstrument = [df['acousticness'].min()]

maxLive = [df['liveness'].max()]
targetLive = [df['liveness'].mean()]
minLive = [df['liveness'].min()]

maxLoud = [df['loudness'].max()]
targetLoud = [df['loudness'].mean()]
minLoud = [df['loudness'].min()]

maxSpeech = [df['speechiness'].max()]
targetSpeech = [df['speechiness'].mean()]
minSpeech = [df['speechiness'].min()]

maxTempo = [df['tempo'].max()]
targetTempo = [df['tempo'].mean()]
minTempo = [df['tempo'].min()]

maxValence = [df['valence'].max()]
targetValence = [df['valence'].mean()]
minValence = [df['valence'].min()]

#determine the two most common genres amongst the playlist
seedGenres = df['artist genres']
seedGenresStr=""
for x in range(0, len(seedGenres)):
        tempList = ast.literal_eval(seedGenres[x])
        for y in range(0, len(tempList)):
            if x == 0 and y == 0:
                seedGenresStr += tempList[y].replace(" ", "-")
            else:
                seedGenresStr += "," + tempList[y].replace(" ", "-")
seedGenresList = seedGenresStr.split(",")
c = Counter(seedGenresList)
seedGenresListMC = c.most_common(2)
seedGenresMCStr = seedGenresListMC[0][0] + "," + seedGenresListMC[1][0]

#convert artists list into a string for the get request to Spotify
seedArtists = df['artist uri']
seedArtistsStr = seedArtists[0]
for x in range(1, len(seedArtists)):
    seedArtistsStr += ("," + seedArtists[x])

#convert tracks list into a string for the get request to Spotify
seedTracks = df['song uri']
seedTracksStr = seedTracks[0]
for x in range(1, len(seedTracks)):
    seedTracksStr += ("," + seedTracks[x])

#using the data from the playlist, determine 5 recommended songs
listOfRecs = sp.recommendations(seed_artists=[seedArtistsStr], seed_genres=[seedGenresMCStr], seed_tracks=[seedTracksStr], limit=5, country=None, min_acousticness=minAcoustic, max_acousticness=maxAcoustic, target_acousticness=targetAcoustic, min_danceability=minDance, max_danceability=maxDance, target_danceability=targetDance, min_energy=minEnergy, max_energy=maxEnergy, target_energy=targetEnergy, min_instrumentalness=minInstrument, max_instrumentalness=maxInstrument, target_instrumentalness=targetInstrument, min_liveness=minLive, max_liveness=maxLive, target_liveness=targetLive, min_loudness=minLoud, max_loudness=maxLoud, target_loudness=targetLoud, min_speechiness=minSpeech, max_speechiness=maxSpeech, target_speechiness=targetSpeech, min_tempo=minTempo, max_tempo=maxTempo, target_tempo=targetTempo, min_valence=minValence, max_valence=maxValence, target_valence=targetValence)

#print the 5 recommended songs based on the playlist
print(get_track_names(listOfRecs['tracks']))
