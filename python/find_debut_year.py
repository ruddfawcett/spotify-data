#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import re
import requests
import hashlib

import pandas as pd
from datetime import datetime, timedelta

master = {}

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
        hash_object = hashlib.md5(query.encode())
        hex_digest = hash_object.hexdigest()
        _id = str(hex_digest)

        if _id in master:
            continue
        else:
            master[_id] = week.strftime('%Y')

def do_work(start_date):
    while True:
        chart = csv.DictReader(open('data/billboard-charts/{0}.csv'.format(start_date)))
        with_ids = process(chart, start_date)

        print('Parsed {0}...'.format(start_date))

        if date_to_str(start_date) == '2018-02-03':
            break
        # switch back to minus after
        start_date = start_date + timedelta(days=7)

# 2016-03-05
do_work(str_to_date('1958-08-02'))

matched_data = csv.DictReader(open('matched_data.csv'))
new_matched_data = []

for entry in matched_data:
    entry['debut_year'] = int(master[entry['id']])
    new_matched_data.append(entry)

master_db = pd.DataFrame(new_matched_data, columns=new_matched_data[0].keys())
master_db.set_index('id', inplace=True)
master_db.to_csv('debut_year_matched.csv')
