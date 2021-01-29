from django.urls import path
from filmsapp import views

app_name = "filmsapp"

urlpatterns = [
    path('', views.MoviesList.as_view(), name="movies_list"),
    path('<int:page>/', views.MoviesList.as_view(), name="movies_list"),
    path('film/<int:pk>/', views.MovieDetail.as_view(), name="movie_detail"),
    path('category/', views.MovieCatalog.as_view(), name='category_list'),
    path('category/<int:pk>/', views.MovieCatalogPK.as_view(), name='film_category'),
    path('genre/', views.MovieGenre.as_view(), name='genre_list'),
    path('genre/<int:pk>/', views.MovieGenrePK.as_view(), name='film_genre'),
    path('participant/<int:pk>/', views.ParticipantDetail.as_view(), name='participant_detail'),
    path('participant/history/<int:pk>/', views.ParticipantHistory.as_view(), name='participant_history'),
]
