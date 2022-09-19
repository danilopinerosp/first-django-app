from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    born = models.DateField()

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genrej = models.CharField(max_length=200)
