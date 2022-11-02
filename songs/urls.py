from django.urls import path
from . import views

urlpatterns = [
    path('',views.Song_library),
    path('<int:pk>/', views.get_song_by_id),

]