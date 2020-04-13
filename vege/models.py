from django.db import models

# Create your models here.


class Blogs(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=64)
    date = models.CharField(max_length=10)
    name = models.CharField(max_length=30, default="Admin")
    head_text = models.CharField(max_length=100, null=False)
    text = models.CharField(max_length=500, null=False)

    def __str__(self):
        return f'{self.id} --> {self.name}, {self.date}'


class RuBlog(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=64)
    date = models.CharField(max_length=10)
    name = models.CharField(max_length=30, default="Admin")
    head_text = models.CharField(max_length=100, null=False)
    text = models.CharField(max_length=500, null=False)

    def __str__(self):
        return f'{self.id} --> {self.name}, {self.date}'


class EnProduct(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    image = models.CharField(max_length=64)
    price = models.IntegerField()
    discount = models.IntegerField(blank=True)
    price_sale = models.FloatField()

    def __str__(self):
        return f'{self.id} --> {self.name}'


class RuProduct(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    image = models.CharField(max_length=64)
    price = models.IntegerField()
    discount = models.IntegerField(blank=True)
    price_sale = models.FloatField()

    def __str__(self):
        return f'{self.id} --> {self.name}'
