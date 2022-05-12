from turtle import title
from .models import Movies


b = Movies( title = "I Love You to Death", 
    language = "en",
    genres = "Action, Comedy, Crime",
    overview= "Joey Boca is the owner of a pizza parlour, and has been married to Rosalie for years. When Rosalie discovers that Joey is a womanizer and has been cheating on her for a long time, she goes to extreme lengths to punish him.",
    popularity = 6.977,
    poster_path = "/8LdWJLUfEa5JeUJ7SljJQMIJikZ.jpg",
    release_date = "1990-04-06",
    vote_average = 6.4,
    vote_count = 192)

b.save()