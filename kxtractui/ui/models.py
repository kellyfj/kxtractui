# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Podcast(models.Model):
    name = models.CharField(max_length=256)
    rss_url = models.CharField(max_length=1024)

    class Meta:
        managed = getattr(settings, 'UNDER_TEST', False)
        db_table = 'podcast'

    def __str__(self):
        return self.name


class Episode(models.Model):
    processing_staus_type = (
        ('0', "Downloaded"),
        ('1', "Transcription In Process"),
        ('2', "Transcription Complete"),
        ('3', "Error"),
    )
    podcast = models.ForeignKey('Podcast', models.DO_NOTHING, null=True)
    id = models.IntegerField(primary_key=True, blank=True)
    episode_name = models.CharField(max_length=128)
    filesize_kb = models.IntegerField(blank=True, null=True)
    origin_url = models.CharField(max_length=256)
    s3_url = models.CharField(max_length=256)
    processing_status = models.CharField(choices=processing_staus_type, max_length=64)

    class Meta:
        managed = getattr(settings, 'UNDER_TEST', False)
        db_table = 'episode'
        unique_together = (('podcast', 'episode_name'),)

    def __str__(self):
        return self.episode_name


class Subscription(models.Model):
    user_id = models.CharField(max_length=64)
    podcast = models.ForeignKey(Podcast, models.DO_NOTHING, null=True)

    class Meta:
        managed = getattr(settings, 'UNDER_TEST', False)
        db_table = 'subscription'

    def __str__(self):
        return "UserId :{} --> Podcast Name: {}.".format(self.user_id, self.podcast.name)


class Transcription(models.Model):
    episode = models.OneToOneField(Episode, models.DO_NOTHING, null=True)
    s3_transcription_download_location = models.CharField(max_length=4096, blank=True, null=True)
    raw_transcription = models.TextField(blank=True, null=True)
    formatted_transcription = models.TextField(blank=True, null=True)

    class Meta:
        managed = getattr(settings, 'UNDER_TEST', False)
        db_table = 'transcription'

    def __str__(self):
        return "Transcription for Episode Name : {}".format(self.episode.episode_name)
