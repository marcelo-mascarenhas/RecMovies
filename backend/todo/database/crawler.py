import tmdbsimple as tmdb
import json

tmdb.API_KEY = ''

def convert(dic):
  string_final = ""
  for d in dic:
      string_final += d['name'] + ","
  string_final = string_final.rstrip(',')
  return string_final

def main():
  content = {}
  for i in range(100000,150000):
    try:
      response = tmdb.Movies(i).info()
      string_convert = convert(response['genres'])
      if(response['release_date'] == ""):
        response['release_date'] = None
      
      content = {"pk": i, "model": "todo.movies","fields": {"title": response['title'],"language": response['original_language'], "genres": string_convert, "overview": response['overview'],"popularity": response['popularity'], "poster_path": response['poster_path'], "release_date": response['release_date'],"vote_average": response['vote_average'],"vote_count":response['vote_count']}}
      list_movies.append(content)
    except:
      continue


list_movies = list()
main()
json_object = json.dumps(list_movies, indent= 4)
with open("sample.json", "w") as outfile:
  outfile.write(json_object)
