#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import re
import requests
import hashlib

import pandas as pd
from datetime import datetime, timedelta

master_dict = csv.DictReader(open('master.csv'))
master_queries = []
master_list = {}

for entry in master_dict:
    if 'query' in entry:
        hash_object = hashlib.md5(entry['query'].encode())
        hex_digest = hash_object.hexdigest()

        entry['peak_pos'] = 101
        entry['peak_week'] = ''
        entry['streak'] = 0
        entry['id'] = hex_digest
        master_list[hex_digest] = entry
        # master_slugs.append(entry['query'])

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

        dsong = master_list[str(hex_digest)]

        if int(song['peak_pos']) < int(dsong['peak_pos']):
            dsong['peak_pos'] = int(song['peak_pos'])
            dsong['peak_week'] = date_to_str(week)

        if int(song['streak']) > int(dsong['streak']):
            dsong['streak'] = int(song['streak'])

        master_list[hex_digest] = dsong

def do_work(start_date):
    while True:
        chart = csv.DictReader(open('data/billboard-charts/{0}.csv'.format(start_date)))
        with_ids = process(chart, start_date)

        print('Parsed {0}...'.format(start_date))
        if date_to_str(start_date) == '2018-02-03':
            break

        start_date = start_date + timedelta(days=7)

    final_list = []

    for key in master_list:
        final_list.append(master_list[key])

    master_db = pd.DataFrame(final_list, columns=final_list[0].keys())
    master_db.set_index('id', inplace=True)
    master_db.to_csv('matched_data.csv')

# 2016-03-05
#
do_work(str_to_date('1958-08-02'))
