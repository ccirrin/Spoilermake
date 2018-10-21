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

@app.route('/environment', methods=['GET', 'POST'])
def environment():
    return render_template('environment.html')

#Run app
if __name__ == '__main__':
    app.run()
