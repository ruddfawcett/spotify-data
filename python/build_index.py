#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import re
import requests

import pandas as pd
from datetime import datetime, timedelta

master_dict = csv.DictReader(open('master.csv'))
master_queries = []
master_list = []

for entry in master_dict:
    if 'query' in entry:
        master_slugs.append(entry['query'])

def str_to_date(s):
    return datetime.strptime(s, '%Y-%m-%d').date()

def date_to_str(date):
    return date.strftime('%Y-%m-%d')

def sanitize(s):
    fix = s.replace('*', '').strip().lower()
    return re.sub(r'\([^)]*\)', '', fix)

def process(chart, week):
    for song in chart:
        stripped_song = sanitize(song['title'])
        stripped_artist = sanitize(song['artist']).split(' ')
        artist = ''

        if stripped_artist[0] == 'the':
            if len(stripped_artist) > 1:
                artist = stripped_artist[1]
            else:
                artist = stripped_artist[0]
        else:
            artist = stripped_artist[0]

        query = 'artist:{0} track:{1}'.format(artist, stripped_song)

        if query in master_queries:
            continue
        else:
            entry = {
                'title': song['title'],
                'artist': song['artist'],
                'query': query,
                'spotify_id': ''
            }

            master_list.append(entry)
            master_queries.append(query)

def do_work(start_date):
    while True:
        chart = csv.DictReader(open('data/billboard-charts/{0}.csv'.format(start_date)))
        with_ids = process(chart, start_date)

        print('Parsed {0}...'.format(start_date))

        if date_to_str(start_date) == '1958-08-02':
            break

        start_date = start_date - timedelta(days=7)

    master_db = pd.DataFrame(master_list, columns=master_list[0].keys())
    master_db.set_index('title', inplace=True)
    master_db.to_csv('master_final_final_query.csv')

# 2016-03-05
do_work(str_to_date('2018-02-03'))
