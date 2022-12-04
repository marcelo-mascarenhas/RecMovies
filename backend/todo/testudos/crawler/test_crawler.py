from todo.crawlers.crawler import Crawler
import pytest

def test_if_strings_are_being_formated_correctly():
    crawler_object = Crawler()
    movies_dictionary = [{'name': 'Wonderland', 'Genre': 'Fantasy'}, 
                        {'name': 'Doctor House', 'Genre': 'Thriller'},
                        {'name': 'Captain Marvel', 'Genre': 'Pimba'}]
    answer = crawler_object.convert_string(movies_dictionary)

    assert answer == 'Wonderland,Doctor House,Captain Marvel'


def test_if_empty_dictionary_raises_exception():
    crawler_object = Crawler()
    movies_dictionary = {}

    with pytest.raises(Exception) as exception:
        crawler_object.convert_string(movies_dictionary)

    assert str(exception.value) == "Empty dictionary"


def test_if_content_is_being_created_correctly():
    crawler_object = Crawler()
    movie = {'title': 'Wonderland', 'original_language': 'en', 'genres': [{'name': 'Fantasy'}], "overview": 
    "Wonderland is a movie that shows the adventures of a girl in a fantasy world", "popularity": 100.0,
    "poster_path": "./img/poster_wonderland", "release_date": "2010-01-01", "vote_average": 10.0, "vote_count": 100000}

    answer = crawler_object.create_content(1, movie)

    assert answer == {"pk": 1,"fields": {"title": "Wonderland", "language": "en", "genres": 
    "Fantasy", "overview": "Wonderland is a movie that shows the adventures of a girl in a fantasy world", "popularity":
    100.0, "poster_path": "./img/poster_wonderland", "release_date": "2010-01-01", "vote_average": 10.0, "vote_count": 100000}, "model": "todo.movies"}


def test_if_release_date_is_treated_correctly():
    crawler_object = Crawler()
    movie = {'title': 'Wonderland', 'original_language': 'en', 'genres': [{'name': 'Fantasy'}], "overview": 
    "Wonderland is a movie that shows the adventures of a girl in a fantasy world", "popularity": 100.0,
    "poster_path": "./img/poster_wonderland", "release_date": "", "vote_average": 10.0, "vote_count": 100000}

    answer = crawler_object.create_content(1, movie)

    assert answer == {"pk": 1,"fields": {"title": "Wonderland", "language": "en", "genres":
    "Fantasy", "overview": "Wonderland is a movie that shows the adventures of a girl in a fantasy world", 
    "popularity": 100.0, "poster_path": "./img/poster_wonderland", "release_date": None, "vote_average": 10.0, "vote_count": 100000}, "model": "todo.movies"}

    
