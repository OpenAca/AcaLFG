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
  name = models.CharField(max_length=255)
  email = models.EmailField(blank=True, null=True)
  description = models.TextField(blank=True, null=True)
  posted_datetime = models.DateTimeField(auto_now_add=True)
  new_group_ok = models.BooleanField(default=False)
  voice_parts = models.ManyToManyField(VoicePart, blank=True, null=True)
  location = models.TextField(blank=True, null=True)
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
  email = models.EmailField(blank=True, null=True)
  group = models.CharField(max_length=255)
  posted_datetime = models.DateTimeField(auto_now_add=True)
  description = models.TextField(blank=True, null=True)
  voice_parts = models.ManyToManyField(VoicePart, blank=True, null=True)
  location = models.TextField(blank=True, null=True)
  latitude = models.FloatField(blank=True, null=True)
  longitude = models.FloatField(blank=True, null=True)
  verification_id = models.CharField(max_length=255)
  is_verified = models.BooleanField(default=False)
  is_public = models.BooleanField(default=False)

  def __unicode__(self):
    return self.group
