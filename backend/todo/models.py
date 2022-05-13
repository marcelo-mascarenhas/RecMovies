from django.db import models

# Atributos do Banco de Dados
'''
    title : STRING (titulo do filme)
    language : CHAR (qual é a lingua nativa do filme)
    genres: STRING (todos os generos do filme separados por virgula
                    EX: Action,Comedy,Drama
                    )
    overview: STRING (sinopse do filme)
    popularity: FLOAT (popularidade do filme)
    poster_path: STRING (extensão final da URL que possui o poster do filme
                        a url fixa é: https://image.tmdb.org/t/p/original
                        apos isso você adiciona o caminho do poster_path
                        )
    release_date: DATE (ano de lançamento do filme YYYY-MM-DD)
    vote_average: FLOAT
    vote_count: INT

    Todos os atributos aceitam valores nulos ou valores em branco.
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

