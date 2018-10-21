from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import Required, AnyOf
from flask_navigation import Navigation
from get_data import *
from get_rec import *
import pandas as pd
import math



app = Flask(__name__)
nav = Navigation(app)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'reallyreallyreallysecretkey'


class analyze_form(FlaskForm):
    uri = StringField(u'Spotify URI: ', validators=[Required()])
    submit = SubmitField(u'Submit')

class compare_form(FlaskForm):
    uri = StringField(u'Spotify URI: ', validators=[Required()])
    uri2 = StringField(u'Spotify URI 2: ', validators=[Required()])
    submit = SubmitField(u'Submit')

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('index.html')

@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    form=analyze_form()
    labels = []
    values = []
    uri = None
    if form.validate_on_submit():
        uri = form.uri.data
        spot_type = detect_type(uri)
        if spot_type == 'artist':
            artisttop = sp.artist_top_tracks(uri)
            tracks = []
            for item in artisttop['tracks']:
                tracks.append(sp.track(item['uri']))
            dataframe = get_tracks_info(tracks)
            labels = ['Danceability', 'Energy', 'Speechiness', 'Acousticness',
            'Instrumentalness', 'Liveness', 'Valence']
            values = [dataframe['danceability'].mean(), dataframe['energy'].mean(),
            dataframe['speechiness'].mean(), dataframe['acousticness'].mean(), dataframe['instrumentalness'].mean(),
            dataframe['liveness'].mean(), dataframe['valence'].mean()]
            title = ""

        elif spot_type =='track':
            dataframe = get_tracks_info([sp.track(uri)])
            labels = ['Danceability', 'Energy', 'Speechiness', 'Acousticness',
            'Instrumentalness', 'Liveness', 'Valence']
            values = [dataframe['danceability'].mean(), dataframe['energy'].mean(),
            dataframe['speechiness'].mean(), dataframe['acousticness'].mean(), dataframe['instrumentalness'].mean(),
            dataframe['liveness'].mean(), dataframe['valence'].mean()]
            title = ""

        elif spot_type == 'album':
            album = sp.album_tracks(uri)
            tracks = []
            for item in album['items']:
                tracks.append(sp.track(item['uri']))
            dataframe = get_tracks_info(tracks)
            labels = ['Danceability', 'Energy', 'Speechiness', 'Acousticness',
            'Instrumentalness', 'Liveness', 'Valence']
            values = [dataframe['danceability'].mean(), dataframe['energy'].mean(),
            dataframe['speechiness'].mean(), dataframe['acousticness'].mean(), dataframe['instrumentalness'].mean(),
            dataframe['liveness'].mean(), dataframe['valence'].mean()]
            title = "dakhbdbhskbd"

        else:
            dataframe = get_tracks_info(get_tracks(uri))
            labels = ['Danceability', 'Energy', 'Speechiness', 'Acousticness',
            'Instrumentalness', 'Liveness', 'Valence']
            values = [dataframe['danceability'].mean(), dataframe['energy'].mean(),
            dataframe['speechiness'].mean(), dataframe['acousticness'].mean(), dataframe['instrumentalness'].mean(),
            dataframe['liveness'].mean(), dataframe['valence'].mean()]
            title = sp.user_playlist(uri.split(':')[2], uri.split(':')[4])['name']

        return render_template('analyze.html', form=form, uri=uri, values=values, labels=labels, title=title)
    return render_template('analyze.html', form=form, uri=uri)

@app.route('/generate', methods=['GET', 'POST'])
def generate():
    form = analyze_form()
    uri = None
    if form.validate_on_submit():
        uri = form.uri.data
        dataframe = get_tracks_info(get_tracks(uri))
        tracklist = rec_list(dataframe)
        return render_template('generate.html', form=form, uri=uri, tracklist=tracklist)
    return render_template('generate.html', form=form, uri=uri)

@app.route('/compare', methods=['GET', 'POST'])
def compare():
    uri = None
    uri2 = None
    form = compare_form()
    if form.validate_on_submit():
        uri = form.uri.data
        uri2 = form.uri2.data
        spot_type = detect_type(uri)
        if spot_type == 'artist':
            artisttop = sp.artist_top_tracks(uri)
            tracks = []
            for item in artisttop['tracks']:
                tracks.append(sp.track(item['uri']))
            dataframe = get_tracks_info(tracks)

            artisttop2 = sp.artist_top_tracks(uri)
            tracks2 = []
            for item in artisttop2['tracks']:
                tracks2.append(sp.track(item['uri']))
            dataframe2 = get_tracks_info(tracks2)

            labels = ['Danceability', 'Energy', 'Speechiness', 'Acousticness',
            'Instrumentalness', 'Liveness', 'Valence']
            values = [[dataframe['danceability'].mean(), dataframe2['danceability'].mean()], 
            [dataframe['energy'].mean(), dataframe2['energy'].mean()],
            [dataframe['speechiness'].mean(), dataframe2['speechiness'].mean()], 
            [dataframe['acousticness'].mean(), dataframe2['acousticness'].mean()], 
            [dataframe['instrumentalness'].mean(), dataframe2['instrumentalness'].mean()],
            [dataframe['liveness'].mean(), dataframe2['liveness'].mean()], 
            [dataframe['valence'].mean(), dataframe2['valence'].mean()]]
            title = ""

        elif spot_type =='track':
            dataframe = get_tracks_info([sp.track(uri)])
            labels = ['Danceability', 'Energy', 'Speechiness', 'Acousticness',
            'Instrumentalness', 'Liveness', 'Valence']
            values = [dataframe['danceability'].mean(), dataframe['energy'].mean(),
            dataframe['speechiness'].mean(), dataframe['acousticness'].mean(), dataframe['instrumentalness'].mean(),
            dataframe['liveness'].mean(), dataframe['valence'].mean()]
            title = ""

        elif spot_type == 'album':
            album = sp.album_tracks(uri)
            tracks = []
            for item in album['items']:
                tracks.append(sp.track(item['uri']))
            dataframe = get_tracks_info(tracks)
            labels = ['Danceability', 'Energy', 'Speechiness', 'Acousticness',
            'Instrumentalness', 'Liveness', 'Valence']
            values = [dataframe['danceability'].mean(), dataframe['energy'].mean(),
            dataframe['speechiness'].mean(), dataframe['acousticness'].mean(), dataframe['instrumentalness'].mean(),
            dataframe['liveness'].mean(), dataframe['valence'].mean()]
            title = "dakhbdbhskbd"

        else:
            dataframe = get_tracks_info(get_tracks(uri))
            labels = ['Danceability', 'Energy', 'Speechiness', 'Acousticness',
            'Instrumentalness', 'Liveness', 'Valence']
            values = [dataframe['danceability'].mean(), dataframe['energy'].mean(),
            dataframe['speechiness'].mean(), dataframe['acousticness'].mean(), dataframe['instrumentalness'].mean(),
            dataframe['liveness'].mean(), dataframe['valence'].mean()]
            title = sp.user_playlist(uri.split(':')[2], uri.split(':')[4])['name']

        return render_template('compare.html', form=form, uri=uri, values=values, labels=labels, title=title)
    return render_template('compare.html', form=form, uri=uri)

#Run app
if __name__ == '__main__':
    app.run()
