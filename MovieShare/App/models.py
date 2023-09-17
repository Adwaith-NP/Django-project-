from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=30)
    img = models.ImageField()
    video_file = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.name
