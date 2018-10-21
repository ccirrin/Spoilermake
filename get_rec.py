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

def getRecommendations(csvName, numOfRecs):
    df = pd.read_csv(csvName)

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

    seedGenres=getSeedGenres(df)
    seedTracks=getSeedTracks(df)
    seedArtists=getSeedArtists(df)

    #using the data from the playlist, determine 5 recommended songs
    listOfRecs = sp.recommendations(seed_artists=[seedArtists], seed_genres=[seedGenres], seed_tracks=[seedTracks], limit=numOfRecs, country=None, min_acousticness=minAcoustic, max_acousticness=maxAcoustic, target_acousticness=targetAcoustic, min_danceability=minDance, max_danceability=maxDance, target_danceability=targetDance, min_energy=minEnergy, max_energy=maxEnergy, target_energy=targetEnergy, min_instrumentalness=minInstrument, max_instrumentalness=maxInstrument, target_instrumentalness=targetInstrument, min_liveness=minLive, max_liveness=maxLive, target_liveness=targetLive, min_loudness=minLoud, max_loudness=maxLoud, target_loudness=targetLoud, min_speechiness=minSpeech, max_speechiness=maxSpeech, target_speechiness=targetSpeech, min_tempo=minTempo, max_tempo=maxTempo, target_tempo=targetTempo, min_valence=minValence, max_valence=maxValence, target_valence=targetValence)

    return listOfRecs

def getDanceability(df):
    maxDance = [df['danceability'].max()]
    targetDance = [df['danceability'].mean()]
    minDance = [df['danceability'].min()]
    return tuple(maxDance, minDance, targetDance)

def getEnergy(df):
    maxEnergy = [df['energy'].max()]
    targetEnergy = [df['energy'].mean()]
    minEnergy = [df['energy'].min()]
    return tuple(maxEnergy, minEnergy, targetEnergy)

def getAcousticness(df):
    maxAcoustic = [df['acousticness'].max()]
    targetAcoustic = [df['acousticness'].mean()]
    minAcoustic = [df['acousticness'].min()]
    return tuple(maxAcoustic, minAcoustic, targetAcoustic)

def getInstrumentalness(df):
    maxInstrument = [df['instrumentalness'].max()]
    targetInstrument = [df['instrumentalness'].mean()]
    minInstrument = [df['acousticness'].min()]
    return tuple(maxInstrument, minInstrument, targetInstrument)

def getLiveness(df):
    maxLive = [df['liveness'].max()]
    targetLive = [df['liveness'].mean()]
    minLive = [df['liveness'].min()]
    return tuple(maxLive, minLive, targetLive)

def getLoudness(df):
    maxLoud = [df['loudness'].max()]
    targetLoud = [df['loudness'].mean()]
    minLoud = [df['loudness'].min()]
    return tuple(maxLoud, minLoud, targetLoud)

def getSpeechiness(df):
    maxSpeech = [df['speechiness'].max()]
    targetSpeech = [df['speechiness'].mean()]
    minSpeech = [df['speechiness'].min()]
    return tuple(maxSpeech, minSpeech, targetSpeech)

def getTempo(df):
    maxTempo = [df['tempo'].max()]
    targetTempo = [df['tempo'].mean()]
    minTempo = [df['tempo'].min()]
    return tuple(maxTempo, minTempo, targetTempo)

def getValence(df):
    maxValence = [df['valence'].max()]
    targetValence = [df['valence'].mean()]
    minValence = [df['valence'].min()]
    return tuple(maxValence, minValence, targetValence)

def getSeedGenres(df):
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
    return seedGenresMCStr

def getSeedArtists(df):
    #convert artists list into a string for the get request to Spotify
    seedArtists = df['artist uri']
    seedArtistsStr = seedArtists[0]
    for x in range(1, len(seedArtists)):
        seedArtistsStr += ("," + seedArtists[x])
    return seedArtistsStr


def getSeedTracks(df):
    #convert tracks list into a string for the get request to Spotify
    seedTracks = df['song uri']
    seedTracksStr = seedTracks[0]
    for x in range(1, len(seedTracks)):
        seedTracksStr += ("," + seedTracks[x])
    return seedTracksStr
