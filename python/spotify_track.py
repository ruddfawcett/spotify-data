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

for song in csv.DictReader(open('debut_year_matched_audio_features.csv')):
    master_list.append(song)

def str_to_date(s):
    return datetime.strptime(s, '%Y-%m-%d').date()

def date_to_str(date):
    return date.strftime('%Y-%m-%d')

def fetch(_id):
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {0}'.format(keys['oauth_token']),
    }

    params = ()

    return requests.get('https://api.spotify.com/v1/audio-features/{0}'.format(_id), headers=headers, params=params).json()

def save():
    try:
        db = pd.DataFrame(master_list, columns=master_list[0].keys())
        db.set_index('id', inplace=True)
        db.to_csv('debut_year_matched_audio_features.csv')
        print('[SUCCESS] Saved 250 songs to file.')
    except Exception as e:
        print("Errored out.")
        print(e)

def process():
    i = 0

    for song in master_list:
        if i == 250:
            save()
            i = 0

        if song['duration_ms'] != '':
            continue

        if len(song['spotify_id']) > 10:
            result = fetch(song['spotify_id'])
            i += 1

            if 'error' in result:
                print(result)
                error = "[ERROR] Error finding features for {0} by {1}...".format(song['title'], song['artist'])
                logging.info(error)
                print(error)
            elif 'type' in result and result['type'] == 'audio_features':
                for key in result:
                    if key == 'type' or key == 'uri' or key == 'id' or key == 'track_href' or key == 'analysis_url':
                        continue
                    else:
                        song[key] = result[key]
                print("[SUCCESS] Found features for {0} by {1}...".format(song['title'], song['artist']))
            else:
                print('[ERROR] Unknown error.')

process()
save()
