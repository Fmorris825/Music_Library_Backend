from django.urls import path,include
from . import views

urlpatterns = [
    path('api/music/',include('music.urls')),
    path('<int:pk>/', views.),

]