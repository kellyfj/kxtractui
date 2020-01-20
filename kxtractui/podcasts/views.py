from django.http import HttpResponse
from django.shortcuts import render
from .models import Podcast


def index(request):
    return HttpResponse("Hello World - you are at the KXtract UI Home page")


def podcasts(request):
    current_podcasts = Podcast.objects.order_by('id')
    context = {
        'current_podcasts': current_podcasts,
    }
    return render(request, 'podcasts/index.html', context)


def episodes(request):
    return HttpResponse("TBD2")


def transcription(request):
    return HttpResponse("TBD3")
