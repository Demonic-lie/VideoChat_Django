from django.db import models

# Create your models here.
class currentchat(models.Model):
    hostname = models.CharField(max_length = 30)
    meetingname = models.CharField(max_length = 30)
    
    def __str__(self):
        return f"Host: {self.hostname} and Meeting ID: {self.meetingname}"
