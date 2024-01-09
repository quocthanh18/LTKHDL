import requests
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

def tmdb_rating(movie):
    response = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key=1703a5b2ccea7445d07e9efd6b3e7775&query={movie}")
    data = response.json()
    if data['results']:
        return [movie, data['results'][0]['vote_average'], data['results'][0]['vote_count']]
    else:
        return [movie, 0, 0]

movies = pd.read_csv('data/processed/data.csv')['title'].tolist()
with ThreadPoolExecutor(max_workers=20) as p:
    data = list(p.map(tmdb_rating, movies))

data = pd.DataFrame(data, columns=['title', 'rating', 'votes'])
data.to_csv('data/processed/tmdb.csv', index=True)
