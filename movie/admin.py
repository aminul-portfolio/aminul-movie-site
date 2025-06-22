from django.contrib import admin
from .models import Movie, MovieLinks, Genre

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'language', 'status', 'rating', 'duration', 'slug', 'created']
    list_filter = ['category', 'language', 'status', 'created']
    search_fields = ['title', 'cast']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(MovieLinks)
class MovieLinksAdmin(admin.ModelAdmin):
    list_display = ['movie', 'type', 'link']

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
