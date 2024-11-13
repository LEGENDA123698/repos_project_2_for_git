from django.urls import path
from .views import *

urlpatterns = [
    path('', film_list, name = "film-list"),
    path('films/<int:film_id>/', chose_film, name = "chose-film"),
    path('seance/<int:seance_id>/', seance, name = "seance"),
]