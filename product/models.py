from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse


class Categories(models.Model):
    title=models.CharField(max_length=100,null=True)

    def __str__(self):
        return f'{self.title}'


class product(models.Model):
    categorey=models.ManyToManyField(Categories,related_name='products')
    slug=models.SlugField(unique=True,blank=True)
    title=models.CharField(max_length=50,null=True)
    descriptiom=models.CharField(max_length=200,null=True)
    price=models.IntegerField()
    image=models.ImageField(upload_to='product/image',null=True)
    body=models.TextField(null=True)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('product:detail',kwargs={'slug':self.slug})

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug=slugify(self.title)
        super().save()
# Create your models here.


