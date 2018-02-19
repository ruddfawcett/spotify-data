#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
import csv
import re
import requests
import logging

import pandas as pd
from datetime import datetime, timedelta

logging.basicConfig(filename='errors.log',level=logging.INFO,format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

keys = yaml.load(open('keys.yml'))
master_list = []
for song in csv.DictReader(open('spotify_new__new_query_final.csv')):
    master_list.append(song)

new_list = []
last_song = ''

def str_to_date(s):
    return datetime.strptime(s, '%Y-%m-%d').date()

def date_to_str(date):
    return date.strftime('%Y-%m-%d')

def fetch(query):
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {0}'.format(keys['oauth_token']),
    }

    params = (
        ('q', query),
        ('type', 'track'),
        ('limit', '3'),
        ('offset', '0'),
    )

    return requests.get('https://api.spotify.com/v1/search', headers=headers, params=params).json()

def save():
    try:
        new_list_db = pd.DataFrame(master_list, columns=master_list[0].keys())
        new_list_db.set_index('title', inplace=True)
        new_list_db.to_csv('spotify_last_pass.csv')
        print('[SUCCESS] Saved 250 songs to file.')
    except Exception as e:
        print("Finished at {0}".format(last_song))
        print(e)

def process():
    i = 0
    # y = 0

    for song in master_list:
        # y += 1

        # if y <= 14790:
        #     continue

        if i == 250:
            save()
            i = 0

        last_song = song['title']
        if len(song['spotify_id']) > 10:
            continue
        else:
            i += 1
            result = fetch(song['query'])

            if 'tracks' in result:
                tracks = result['tracks']
                if len(tracks['items']) == 0:
                    error = "[WARNING] Couldn't find {0} by {1}...".format(song['title'], song['artist'])
                    logging.info(error)
                    print(error)
                else:
                    trackID = tracks['items'][0]['id']
                    song['spotify_id'] = trackID
                    print("[SUCCESS] Found {0} as ID for {1} by {2}...".format(trackID, song['title'], song['artist']))
            else:
                error = "[ERROR] Error finding tracks for {0} by {1}...".format(song['title'], song['artist'])
                logging.info(error)
                print(error)

        # new_list.append(song)

process()
save()
