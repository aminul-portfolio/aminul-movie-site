from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from . import views

from .views import (
    MovieList,
    MovieDetail,
    MovieCategory,
    MovieLanguage,
    MovieSearch,
    MovieYear,
    AboutPage,
    signup_view,
    login_view,
    logout_view,
    dashboard_view,
)

app_name = 'movie'

urlpatterns = [
    path('', MovieList.as_view(), name="movie_list"),
    path('category/<str:category>/', MovieCategory.as_view(), name="movie_category"),
    path('language/<str:lang>/', MovieLanguage.as_view(), name="movie_language"),
    path('search/', MovieSearch.as_view(), name="movie_search"),
    path('about/', AboutPage.as_view(), name="about"),
    path('year/<int:year>/', MovieYear.as_view(), name='movie_year'),

    # 🔐 Auth
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),

    # 🔐 Password Reset
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='movie/password_reset_confirm.html',
            success_url=reverse_lazy('movie:login')  # 🔁 redirect to login page
        ),
        name='password_reset_confirm'
    ),

    # Other auth views (for reference)
    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='movie/password_reset_form.html',
            email_template_name='movie/password_reset_email.html',
            subject_template_name='movie/password_reset_subject.txt',
            success_url=reverse_lazy('movie:password_reset_done')
        ),
        name='password_reset'
    ),
    path(
        'password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='movie/password_reset_done.html'
        ),
        name='password_reset_done'
    ),
    # 🎬 Movie detail last!
    path('<slug:slug>/', MovieDetail.as_view(), name="movie_detail"),

]

