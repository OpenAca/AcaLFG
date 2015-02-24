from django.db import models
from django.contrib.auth.models import User

class VoicePart(models.Model):
  """An a cappella voice part."""
  name = models.CharField(max_length=50)

  def __unicode__(self):
    return self.name


class UserLFG(models.Model):
  """A single user looking for a group to join."""
  user = models.ForeignKey(User, blank=True, null=True)
  name = models.CharField(
      max_length=255, help_text='Your name (first only is ok!)')
  email = models.EmailField()
  description = models.TextField()
  posted_datetime = models.DateTimeField(auto_now_add=True)
  new_group_ok = models.BooleanField(
      default=False,
      help_text='Would you be ok with helping to start a new group?')
  voice_parts = models.ManyToManyField(
      VoicePart, blank=True, null=True, verbose_name='Voice part(s)',
      help_text='Select any and all that apply!')
  location = models.TextField(help_text='"City, State" or "City, Country"')
  latitude = models.FloatField(blank=True, null=True)
  longitude = models.FloatField(blank=True, null=True)
  verification_id = models.CharField(max_length=255)
  is_verified = models.BooleanField(default=False)
  is_public = models.BooleanField(default=False)

  def __unicode__(self):
    return self.email


class Audition(models.Model):
  """An audition for a group."""
  posted_by = models.ForeignKey(User, blank=True, null=True)
  email = models.EmailField()
  group = models.CharField(max_length=255, verbose_name='Group Name')
  posted_datetime = models.DateTimeField(auto_now_add=True)
  description = models.TextField()
  voice_parts = models.ManyToManyField(
      VoicePart, blank=True, null=True, verbose_name='Voice part(s)')
  location = models.TextField(help_text='"City, State" or "City, Country"')
  latitude = models.FloatField(blank=True, null=True)
  longitude = models.FloatField(blank=True, null=True)
  verification_id = models.CharField(max_length=255)
  is_verified = models.BooleanField(default=False)
  is_public = models.BooleanField(default=False)

  def __unicode__(self):
    return self.group
