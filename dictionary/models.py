from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Tag(models.Model):
    value = models.CharField(max_length=32, unique=True)

    def __str__(self):

        return self.value


class PersonalDictionary(models.Model):
    owner = models.OneToOneField(to=User, on_delete=models.CASCADE)

    def size(self):

        return self.elp.objects.count()

    def __str__(self):
        owner_name = self.owner.username

        return f"{owner_name}'s dictionary"


class Entry(models.Model):
    word = models.CharField(max_length=128)
    definition = models.TextField(blank=True)
    tags = models.ManyToManyField(to=Tag, blank=True)
    synonyms = models.ManyToManyField(to="Entry", related_name="syn", blank=True)
    antonyms = models.ManyToManyField(to="Entry", related_name="ant", blank=True)

    def __str__(self):

        return self.word

    class Meta:
        ordering = ['word']


class EntryLearningProgress(models.Model):
    personal_dictionary = models.OneToOneField(to=PersonalDictionary,
                                               related_name="elp",
                                               null=True,
                                               on_delete=models.CASCADE)
    entry = models.ForeignKey(to=Entry,
                              on_delete=models.CASCADE)

    @property
    def successful_attempts(self):

        return self.attempt_set.filter(successful=True).count()

    @property
    def unsuccessful_attempts(self):

        return self.attempt_set.filter(successful=False).count()


class Attempt(models.Model):
    progress = models.ForeignKey(to=EntryLearningProgress,
                                 on_delete=models.CASCADE)
    successful = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        result = "Unsuccessful" if not self.successful else "Successful"

        return f"{result} attempt at {self.date_created}"


class Example(models.Model):
    text = models.TextField()
    entry = models.ForeignKey(to=Entry, on_delete=models.CASCADE)
    author = models.CharField(max_length=64, default="Unknown author")
    source = models.CharField(max_length=128, default="unknown source")

    def __str__(self):

        return self.text
