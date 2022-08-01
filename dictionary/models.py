from django.db import models


class Entry(models.Model):
    word = models.CharField(max_length=128)
    definition = models.TextField()

    def __str__(self):
        return self.word
