from django.db import models
from django.utils.text import slugify
from django.utils import timezone

# Category choices
CATEGORY_CHOICES = (
    ('action', 'Action'),
    ('drama', 'Drama'),
    ('comedy', 'Comedy'),
    ('romance', 'Romance'),
)

LANGUAGE_CHOICES = (
    ('english', 'English'),
    ('german', 'German'),
)

STATUS_CHOICES = (
    ('RA', 'Recently Added'),
    ('MW', 'Most Watched'),
    ('TR', 'Top Rated'),
)

LINK_CHOICES = (
    ('D', 'Download Link'),
    ('W', 'Watch Link'),
)

# 🎭 New Genre model
class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# 🎬 Movie model
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='movies/')
    banner = models.ImageField(upload_to='movies_banner/')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=15)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2)
    cast = models.TextField()  # ✅ More space for full cast list
    year_of_production = models.DateField()
    duration = models.PositiveIntegerField(help_text="Duration in minutes")  # ✅ New
    rating = models.FloatField(default=0.0)  # ✅ New
    trailer_url = models.URLField(blank=True, null=True)  # ✅ New
    genres = models.ManyToManyField(Genre, blank=True)  # ✅ New
    views_count = models.IntegerField(default=0)
    created = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Movie, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

# 🔗 Watch/Download links
class MovieLinks(models.Model):
    movie = models.ForeignKey(Movie, related_name='movie_watch_links', on_delete=models.CASCADE)
    type = models.CharField(choices=LINK_CHOICES, max_length=1)
    link = models.URLField()

    def __str__(self):
        return f"{self.get_type_display()} - {self.movie.title}"
