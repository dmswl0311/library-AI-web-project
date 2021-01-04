from django.db import models

class LibraryList(models.Model):
    ISBN = models.IntegerField(default=0)
    year = models.IntegerField(default=0)
    book_name = models.TextField(blank=True)
    author = models.TextField(blank=True)
    explain = models.TextField(blank=True)
    url = models.TextField(blank=True)
    gender = models.CharField(max_length=10)
    age = models.IntegerField(default=0)
    category_rank = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    category_name = models.TextField(blank=True)
