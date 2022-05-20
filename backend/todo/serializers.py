from rest_framework import serializers
from .models import Movies

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ('title', 'language', 'genres', 'overview', 'popularity' ,'poster_path','release_date','vote_average','vote_count')