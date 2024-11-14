import pandas as pd

def import_dataset(src):
    try:
        return pd.read_csv(src)
    except FileNotFoundError:
        print('The ' +  src + ' file was not found.')
    except pd.errors.EmptyDataError:
        print('The ' + src + ' file is empty.')
    except pd.errors.ParserError:
        print('The ' + src + ' file: parser error.')

def convert_timestamp(dataFrame, column, timeUnit):
    dataFrame[column] = pd.to_datetime(dataFrame[column], unit=timeUnit)

if __name__ == "__main__":
    movies = import_dataset('ml-latest-small/movies.csv')
    ratings = import_dataset('ml-latest-small/ratings.csv')
    tags = import_dataset('ml-latest-small/tags.csv')
    convert_timestamp(tags, 'timestamp', 's')
    convert_timestamp(ratings, 'timestamp', 's')
    ratings_avg = ratings.groupby('movieId')['rating'].agg(['count','mean'])
    movies = pd.merge(movies, ratings_avg, on='movieId')
