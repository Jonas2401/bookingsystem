from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    title = models.CharField(max_length=255, db_index=True)
    start_time = models.DateTimeField(db_index=True)
    end_time = models.DateTimeField(db_index=True)
    priority = models.IntegerField()

class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    booker = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    confirmed = models.BooleanField(default=False)

class ShareableLink(models.Model):
    token = models.CharField(max_length=32, unique=True)
    limit = models.IntegerField()
    used = models.IntegerField(default=0)
