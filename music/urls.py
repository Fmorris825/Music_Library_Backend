from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.music_library),
    path('<int:pk>/', views.get_song_by_id),

]