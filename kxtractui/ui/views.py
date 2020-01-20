from django.http import HttpResponse
from django.shortcuts import render
from .models import Podcast, Episode


def index(request):
    return HttpResponse("Hello World - you are at the KXtract UI Home page")


def podcasts(request):
    current_podcasts = Podcast.objects.order_by('id')
    context = {
        'current_podcasts': current_podcasts,
    }
    return render(request, 'podcasts/index.html', context)


def episodes(request):
    episodes = Episode.objects.order_by('id')
    context = {
        'episodes': episodes,
    }
    return render(request, 'episodes/index.html', context)


def transcription(request):
    return HttpResponse("TBD3")
