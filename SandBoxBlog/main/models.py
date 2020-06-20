from django.db import models
from django.utils import timezone

class TimeStamped(models.Model):
    creation_date = models.DateTimeField()
    last_modified = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = timezone.now()

        self.last_modified = timezone.now()
        return super(TimeStamped, self).save(*args, **kwargs)

    class Meta:
        abstract = True

class Post(TimeStamped):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    content = models.CharField(max_length=2000)

    def __str__(self):
        return self.title