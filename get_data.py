from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import json
import requests
import pandas as pd

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

uri = 'spotify:user:9mtj6p9tgugxw8r33lmd5ef1k:playlist:5zmZ6CrKifQOtx6wJGhOG9'

#uri is the uri of the playlist you wish to analyze
def get_tracks(uri):
    tracks = []
    username = uri.split(':')[2]
    playlist_id = uri.split(':')[4]
    results = sp.user_playlist_tracks(username, playlist_id)
    for item in results['items']:
        tracks.append(item['track'])
    return(tracks)

#tracks is list of tracks
def get_track_uris(tracks):
    uris = []
    for item in tracks:
        uris.append(item['uri'])
    return(uris)

#tracks is list of tracks
def get_track_names(tracks):
    names = []
    for item in tracks:
        names.append(item['name'])
    return(names)

#uris is list of uris
def get_audio_features(uris):
    audio_features = []
    for uri in uris:
        audio_features.append(sp.audio_features(uri))
    return(audio_features)

#uris is list of uris
def get_audio_analysis(uris):
    audio_analysis = []
    for uri in uris:
        audio_analysis.append(sp.audio_analysis(uri))
    return(audio_analysis)

def get_tracks_info(tracks):
    columns = ['song', 'song uri', 'artist', 'artist uri', 'artist genres', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature']
    df = pd.DataFrame(columns=columns)
    i = 0
    for track in tracks:
        features = sp.audio_features(track['uri'])
        df.loc[i, 'song'] = track['name']
        df.loc[i, 'song uri'] = track['uri']
        df.loc[i, 'artist'] = track['artists'][0]['name']
        df.loc[i, 'artist uri'] = track['artists'][0]['uri']
        df.loc[i, 'artist genres'] = sp.artist(track['artists'][0]['uri'])['genres']
        df.loc[i, 'danceability'] = features[0]['danceability']
        df.loc[i, 'energy'] = features[0]['energy']
        df.loc[i, 'key'] = features[0]['key']
        df.loc[i, 'loudness'] = features[0]['loudness']
        df.loc[i, 'mode'] = features[0]['mode']
        df.loc[i, 'speechiness'] = features[0]['speechiness']
        df.loc[i, 'acousticness'] = features[0]['acousticness']
        df.loc[i, 'instrumentalness'] = features[0]['instrumentalness']
        df.loc[i, 'liveness'] = features[0]['liveness']
        df.loc[i, 'valence'] = features[0]['valence']
        df.loc[i, 'tempo'] = features[0]['tempo']
        df.loc[i, 'duration_ms'] = features[0]['duration_ms']
        df.loc[i, 'time_signature'] = features[0]['time_signature']
        i += 1
    return(df)

