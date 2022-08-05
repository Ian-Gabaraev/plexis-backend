from django.db import models


class Entry(models.Model):
    #  TODO: Add tags like "SAT1000" etc.
    word = models.CharField(max_length=128)
    definition = models.TextField()

    def __str__(self):
        return self.word

    class Meta:
        ordering = ['word']


class Example(models.Model):
    text = models.TextField()
    entry = models.ForeignKey(to=Entry, on_delete=models.CASCADE)
    author = models.CharField(max_length=64, default="Unknown author")
    source = models.CharField(max_length=128, default="unknown source")

    def __str__(self):
        return self.text


class Tag(models.Model):
    value = models.CharField(max_length=32)
    entry = models.ManyToManyField(to=Entry, blank=True)

    def __str__(self):
        return self.value
