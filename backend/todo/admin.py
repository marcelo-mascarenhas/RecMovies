from django.contrib import admin
from .models import Movies

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'overview', 'poster_path')

# Register your models here.
admin.site.disable_action('delete_selected')
admin.site.register(Movies, TodoAdmin)