from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import json
import requests

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

def get_track_uris(tracks):
    uris = []
    for item in tracks:
        uris.append(item['uri'])
    return(uris)

def get_audio_features(uris):
    audio_features = []
    for uri in uris:
        audio_features.append(sp.audio_features(uri))
    return(audio_features)

def get_audio_analysis(uris):
    audio_analysis = []
    for uri in uris:
        audio_analysis.append(sp.audio_analysis(uri))
    return(audio_analysis)

print(get_track_uris(get_tracks(uri)))
