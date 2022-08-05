from django.db import models


class Entry(models.Model):
    word = models.CharField(max_length=128)
    definition = models.TextField()

    def __str__(self):
        return self.word

    class Meta:
        ordering = ['word']


class Example(models.Model):
    text = models.TextField()
    entry = models.ForeignKey(to=Entry, on_delete=models.CASCADE)
    author = models.CharField(max_length=64)
    source = models.CharField(max_length=128)

    def __str__(self):
        return self.text
