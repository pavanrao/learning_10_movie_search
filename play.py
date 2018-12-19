import requests
import collections

MovieResults = collections.namedtuple(
    "MovieResult",
    "imdb_code,title,duration,director,year,rating,imdb_score,keywords,genres",
)

search = input("What movie do you want to search for: ")
url = "http://movie_service.talkpython.fm/api/search/{}".format(search)

response = requests.get(url)

movie_data = response.json()

movies_list = movie_data.get("hits")

# movies = []
# for md in movies_list:
#     m = MovieResults(
#         imdb_code=md.get('imdb_code'),
#         title=md.get('title'),
#         duration=md.get('duration'),
#         director=md.get('director'),
#         year=md.get('year',0),
#         rating=md.get('rating', 0),
#         imdb_score=md.get('imdb_score',0.0),
#         keywords=md.get('keywords'),
#         genres=md.get('genres')
#     )
#     movies.append(m)


movies = [
    MovieResults(**md)
    for md in movies_list
]

print("Found {} movies for search {}".format(len(movies),search))

for m in movies:
    print("{} == {} ".format(m.year, m.title))




