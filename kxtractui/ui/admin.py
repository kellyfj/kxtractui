from django.contrib import admin

from .models import Podcast, Episode, Subscription, Transcription

admin.site.register(Podcast)
admin.site.register(Episode)
admin.site.register(Subscription)
admin.site.register(Transcription)

