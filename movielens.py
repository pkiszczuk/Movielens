import pandas as pd

movies = pd.read_csv('ml-latest-small/movies.csv')
ratings = pd.read_csv('ml-latest-small/ratings.csv')
tags = pd.read_csv('ml-latest-small/tags.csv')

tags['timestamp'] = pd.to_datetime(tags['timestamp'], unit='s')

ratings['timestamp'] = pd.to_datetime(ratings['timestamp'], unit='s')
