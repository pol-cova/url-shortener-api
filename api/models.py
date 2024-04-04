from django.db import models

# class Url
class Url(models.Model):
    key = models.CharField(max_length=6, unique=True)
    url = models.URLField(max_length=2000)
    short_url = models.URLField(max_length=2000, blank=True)

    def __str__(self):
        return f'{self.key} -> {self.url}'