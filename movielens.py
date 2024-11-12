import pandas as pd

movies = pd.read_csv('ml-latest-small/movies.csv')
ratings = pd.read_csv('ml-latest-small/ratings.csv')
tags = pd.read_csv('ml-latest-small/tags.csv')

tags['timestamp'] = pd.to_datetime(tags['timestamp'], unit='s')

ratings['timestamp'] = pd.to_datetime(ratings['timestamp'], unit='s')

ratings_avg = ratings.groupby('movieId')['rating'].agg(['count','mean'])

print(ratings_avg)

movies = pd.merge(movies, ratings_avg, on='movieId')

print(movies.head())