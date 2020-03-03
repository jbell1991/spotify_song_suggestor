from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from sqlalchemy import create_engine
import sqlite3

DB = SQLAlchemy()


class Songs(DB.Model):
    #Tell SQLAlchemy what the table name is and if there's any table-specific arguments it should know about
    id = DB.Column(DB.BigInteger, primary_key=True)
    genre = DB.Column(DB.String(50))
    artist_name = DB.Column(DB.String(50))
    track_name = DB.Column(DB.String(100))
    track_id = DB.Column(DB.String(50))
    popularity = DB.Column(DB.Integer)
    acousticness = DB.Column(DB.Float)
    danceability = DB.Column(DB.Float)
    duration_ms = DB.Column(DB.Integer)
    energy = DB.Column(DB.Float)
    instrumentalness = DB.Column(DB.Float)
    key = DB.Column(DB.Integer)
    liveness = DB.Column(DB.Float)
    loudness = DB.Column(DB.Float)
    mode = DB.Column(DB.Integer)
    speechiness = DB.Column(DB.Float)
    tempo = DB.Column(DB.Float)
    time_signature = DB.Column(DB.Integer)
    valence = DB.Column(DB.Float)

    def __repr__(self):
        return '<Song {}>'.format(self.track_name)

engine = create_engine('sqlite:///Spotify_Songs.db')
Songs.metadata.create_all(engine)
file_name = 'https://raw.githubusercontent.com/aguilargallardo/DS-Unit-2-Applied-Modeling/master/data/SpotifyFeatures.csv'
df = pd.read_csv(file_name)
DB = df.to_sql(con=engine, index_label='id',
                   name=Songs.__tablename__, if_exists='replace')
