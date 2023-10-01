from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Event(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=1000)
    time = models.TimeField(default=timezone.now().time())
    date = models.DateField(default=timezone.now().date())
    description = models.TextField(max_length=10000)

    ongoing = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
    

class Contribution(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE)
    contributors = models.ManyToManyField(User)

    def __str__(self) -> str:
        return f"{self.contributors} - {self.event.title}"