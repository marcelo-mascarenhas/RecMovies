import tmdbsimple as tmdb
import json

tmdb.API_KEY = ''

class Crawler:
  def __init__(self):
    self.movies = list()
    self.minDataRead = 100000
    self.maxDataRead = 150000

  def convert_string(self,dic):
    string_final = ""
    for d in dic:
        string_final += d['name'] + ","
    return string_final.rstrip(',')

  def format_data(self):
    content = {}
    for i in range(self.minDataRead,self.maxDataRead):
      try:
        response = tmdb.Movies(i).info()
        content = {"pk": i, "model": 
          "todo.movies","fields": {
              "title": response['title'],
              "language": response['original_language'], 
              "genres": self.convert_string(response['genres']), 
              "overview": response['overview'],
              "popularity": response['popularity'], 
              "poster_path": response['poster_path'], 
              "release_date": None if response['release_date'] == "" else response['release_date'],
              "vote_average": response['vote_average'],
              "vote_count":response['vote_count']}
        }
        self.movies.append(content)
      except:
        continue
    
    return json.dumps(self.movies, indent = 4)

if __name__ == "__main__":
  crawler = Crawler()
  json_object = crawler.format_data()
  with open("sample.json", "w") as outfile:
    outfile.write(json_object)
