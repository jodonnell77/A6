"""
A script for clustering spotify songs

This file uses k-means to cluster spotify songs. 

Author: Nicholas James Doyle (njd67)
Date:   March 25, 2019
"""

import spotipy
import spotipy.util
import a6dataset
import a6algorithm

your_client_id = 'INSERT YOUR ID HERE'
your_secret_client_id  = 'INSERT YOUR SECRET ID HERE'
username = 'INSERT YOUR USERNAME ID HERE'
playlist = 'INSERT PLAYLIST ID HERE'
token = spotipy.util.prompt_for_user_token(username,'user-library-read playlist-modify-public',client_id=your_client_id,client_secret=your_secret_client_id, redirect_uri='http://localhost/')

sp = spotipy.Spotify(auth=token)

ids = set([])
results = sp.user_playlist(username,playlist)
for item in results['tracks']['items']:
        ids.add(item['track']['uri'])
ids = list(ids)
current = 0
features = {}
dimensions = [
    'acousticness',
    'danceability',
    'energy',
    'instrumentalness',
    'key',
    'liveness',
    'loudness',
    'mode',
    'speechiness',
    'tempo',
    'time_signature',
    'valence'
]
song_names = []
song_vectors = []
while current < len(ids):
        section = ids[current:current+50]
        results = sp.audio_features(tracks=section)
        for song in results:
                point = []
                for vector in dimensions:
                        point.append(song[vector])
                features[song['uri']] = point
                song_names.append(song['uri'])
                song_vectors.append(point)
        current += 50

name = '{}: Cluster {}'

dset = a6dataset.Dataset(len(song_vectors[0]), song_vectors)
dset.standardize()
k = 2 # number of clusters
limit = 500
iterations = 50 # number of times does k-means 
clusters = []
error = -1
for x in range(iterations):
        km = a6algorithm.Algorithm(dset, k)
        km.run(limit)
        temp_error = km.findTotalError()
        if error == -1 or temp_error < error:
                error = temp_error
                clusters = km.getClusters()
        
ids = []
for x in range(len(clusters)):
        playlist = sp.user_playlist_create(username,name.format("CS 1110 A6", x))
        indices = (clusters[x]).getIndices()
        songs = []
        for y in indices:
                songs.append(song_names[y])
        sp.user_playlist_add_tracks(username, playlist['uri'], songs)