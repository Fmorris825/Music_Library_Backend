from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import MusicSerializers
from .models import Music

# Create your views here.


@api_view(['GET', 'POST'])
def music_library(request):
    
    if request.method == 'GET':
        music = Music.objects.all()
        serializer = MusicSerializers(music, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = MusicSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.errors, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def get_song_by_id(request, pk):
    music = get_object_or_404(Music, pk=pk)
    if request.method == 'GET':
        serializer = MusicSerializers(music)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = MusicSerializers(music, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        music.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)