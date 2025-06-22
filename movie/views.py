from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic import ListView
from django.db.models import Q
from .models import Movie, MovieLinks, Genre

from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# ℹ️ About Page
class AboutPage(TemplateView):
    template_name = 'movie/about.html'

# 🚫 Custom 404
def custom_404_view(request, exception):
    return render(request, 'movie/404.html', status=404)

# 🏠 Home View (limited to 5 per section)
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'movie/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recently_added'] = Movie.objects.filter(status='RA').order_by('-created')[:5]
        context['top_rated'] = Movie.objects.filter(status='TR').order_by('-rating')[:5]
        context['most_watched'] = Movie.objects.filter(status='MW').order_by('-views_count')[:5]
        context['slider_movies'] = Movie.objects.filter(banner__isnull=False).order_by('-created')[:5]
        return context


# 🎞️ All Movies with Filters
class MovieList(ListView):
    model = Movie
    template_name = 'movie/movie_list.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        year = self.request.GET.get('year')
        genre = self.request.GET.get('genre')
        sort = self.request.GET.get('sort')
        status = self.request.GET.get('status')

        if category:
            queryset = queryset.filter(category=category)
        if year:
            try:
                year_int = int(year)
                queryset = queryset.filter(year_of_production__year=year_int)
            except ValueError:
                pass
        if genre:
            queryset = queryset.filter(genres__name__iexact=genre)
        if status:
            queryset = queryset.filter(status=status)
        if sort == 'rating':
            queryset = queryset.order_by('-rating')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['selected_category'] = self.request.GET.get('category', '')
        context['selected_year'] = self.request.GET.get('year', '')
        context['selected_genre'] = self.request.GET.get('genre', '')
        context['selected_sort'] = self.request.GET.get('sort', '')
        context['selected_status'] = self.request.GET.get('status', '')
        context['genres'] = Genre.objects.all()
        context['years'] = Movie.objects.dates('year_of_production', 'year', order='DESC')
        return context

# 🎥 Movie Detail using Slug + View Count + Related
class MovieDetail(DetailView):
    model = Movie
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_object(self):
        obj = super().get_object()
        obj.views_count += 1
        obj.save()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movie = self.get_object()
        context['links'] = MovieLinks.objects.filter(movie=movie)
        context['related_movies'] = Movie.objects.filter(category=movie.category).exclude(id=movie.id)[:6]
        return context

# 🎭 Filter by Category
class MovieCategory(ListView):
    model = Movie
    paginate_by = 5

    def get_queryset(self):
        self.category = self.kwargs['category']
        return Movie.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movie_category'] = self.category
        return context

# 🌍 Filter by Language
class MovieLanguage(ListView):
    model = Movie
    paginate_by = 5

    def get_queryset(self):
        self.language = self.kwargs['lang']
        return Movie.objects.filter(language=self.language)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movie_language'] = self.language
        return context

# 🔍 Search by title, cast, or description
class MovieSearch(ListView):
    model = Movie
    paginate_by = 5
    template_name = 'movie/movie_search.html'

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            return Movie.objects.filter(
                Q(title__icontains=query) |
                Q(cast__icontains=query) |
                Q(description__icontains=query)
            )
        return Movie.objects.none()

# 📅 Archive by Year
class MovieYear(ListView):
    model = Movie
    template_name = 'movie/movie_list.html'
    paginate_by = 5

    def get_queryset(self):
        self.year = self.kwargs['year']
        return Movie.objects.filter(year_of_production__year=self.year)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['selected_year'] = self.year
        context['genres'] = Genre.objects.all()
        context['years'] = Movie.objects.dates('year_of_production', 'year', order='DESC')
        return context





# 🔐 Signup View
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after signup
            return redirect('movie:dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'movie/signup.html', {'form': form})

# 🔐 Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('movie:dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'movie/login.html', {'form': form})

# 🚪 Logout View
def logout_view(request):
    logout(request)
    return redirect('movie:login')

# 👤 Protected Dashboard View
@login_required
def dashboard_view(request):
    return render(request, 'movie/dashboard.html')
