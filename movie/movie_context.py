from .models import Movie

def slider_movies(request):
    movies = Movie.objects.filter(status='RA').order_by('-created')[:7]
    return {"slider_movies": movies}
