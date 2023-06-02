from django.db import models
from datetime import date

class Book(models.Model):
    title = models.CharField(max_length=80)
    author = models.CharField(max_length=50)
    desc = models.TextField(max_length=225)
    pub_date = models.DateField(default=date.today)

    def __str__(self):
        return "%s - %s" % (self.title, self.author)

    def getPubDate():
        pass


