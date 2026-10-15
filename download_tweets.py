
"""Download the lab's fixed archive snapshot into the current folder."""

from urllib.request import urlretrieve
from zipfile import ZipFile
from pathlib import Path

for year in range(2009, 2019):
    filename = f'master_{year}.json.zip'
    json_filename = f'master_{year}.json'

    url = ('https://raw.githubusercontent.com/bpb27/trump_tweet_data_archive/'
           '4b156c24e44815a12da839641bb6c18542345f10/')

    if Path(json_filename).exists():
        print('Skipping', json_filename)
        continue

    print('Downloading', filename)
    urlretrieve(url + filename, filename)

    with ZipFile(filename) as archive:
        archive.extractall('.')
