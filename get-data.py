from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import json
import requests

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

uri = 'spotify:user:9mtj6p9tgugxw8r33lmd5ef1k:playlist:5zmZ6CrKifQOtx6wJGhOG9'

#uri is the uri of the playlist you wish to analyze
def get_track_uris(uri):
    uris = []
    username = uri.split(':')[2]
    playlist_id = uri.split(':')[4]
    results = sp.user_playlist_tracks(username, playlist_id)
    for item in results['items']:
        uris.append(item['track']['uri'])
    return(uris)

print(get_track_uris(uri))
