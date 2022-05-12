from django.db import models

# Create your models here.

#gêneros, linguagem, título, overview, popularidade, vote average e vote count release date

'''
[
    {
        "title": "I Love You to Death",
         "original_language": "en",
        "genres": [
            {
                "id": 28,
                "name": "Action"
            },
            {
                "id": 35,
                "name": "Comedy"
            },
            {
                "id": 80,
                "name": "Crime"
            }
        ],
        "id": 3101,
        "overview": "Joey Boca is the owner of a pizza parlour, and has been married to Rosalie for years. When Rosalie discovers that Joey is a womanizer and has been cheating on her for a long time, she goes to extreme lengths to punish him.",
        "popularity": 6.977,
        "poster_path": "/8LdWJLUfEa5JeUJ7SljJQMIJikZ.jpg",
        "release_date": "1990-04-06",     
        "vote_average": 6.4,
        "vote_count": 192
    }
]
'''

class Movies(models.Model):
    title = models.CharField(max_length=120,blank=True, null=True)
    language = models.CharField(max_length=5,blank=True, null=True)
    genres = models.CharField(max_length=120,blank=True, null=True)
    overview = models.TextField(blank=True, null=True)
    popularity = models.FloatField(blank=True, null=True)
    poster_path = models.CharField(max_length = 200,blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    vote_average = models.FloatField(blank=True, null=True)
    vote_count = models.IntegerField(blank=True, null=True)

    def _str_(self):
        return self.title

