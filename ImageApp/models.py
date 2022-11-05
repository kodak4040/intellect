from django.db import models

# Create your models here.
class Categories(models.Model):
    title = models.CharField(max_length = 100)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = 'categories'

class Profile(models.Model):
    tech_stack = models.ForeignKey(Categories,on_delete = models.CASCADE)    
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to = 'Files/') 
    description = models.TextField(null = True,blank = True)   

    def __str__(self):
        return f'{self.name}'


class Book(models.Model):
    title = models.CharField(max_length=100)
    image = models.FileField(upload_to = 'Files/')
    description = models.TextField(default = '')
    price = models.IntegerField()
    discount = models.IntegerField()
    isbn = models.CharField(max_length=100, unique=True)
    is_published = models.BooleanField(default = True)
    ratings = models.IntegerField()

    def __str__(self):
        return self.title