import requests
import collections

MovieResults = collections.namedtuple(
    "MovieResult",
    "imdb_code,title,duration,director,year,rating,imdb_score,keywords,genres",
)


def find_mpovies(search_text):

    if not search_text or not search_text.strip():
        raise ValueError("Search text is required.")

    url = "http://movie_service.talkpython.fm/api/search/{}".format(search_text)

    response = requests.get(url)
    response.raise_for_status()

    movie_data = response.json()
    movies_list = movie_data.get("hits")

    movies = [
        MovieResults(**md)
        for md in movies_list
    ]

    return movies



