from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('podcasts/', views.podcasts, name='podcasts'),
  path('episodes/', views.episodes, name='episodes'),
  path('episode/<int:episode_id>/transcription/', views.transcription, name='transcription')

]

