from ..models import Movies

def remove_adult():
    forbidden_list = ['sex', 'porn', 'sexo', 'porno','sexo','nude']
    for item in forbidden_list:
      Movies.objects.filter(title__contains=item).delete()
      Movies.objects.filter(overview__contains=item).delete()
