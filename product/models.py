from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse


class Categories(models.Model):
    title=models.CharField(max_length=100,null=True)

    def __str__(self):
        return f'{self.title}'


class Size(models.Model):
    title=models.CharField(max_length=10)

    def __str__(self):
        return f"{self.title}"


class Color(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.title}"


class product(models.Model):
    categorey=models.ManyToManyField(Categories,related_name='products')
    slug=models.SlugField(unique=True,blank=True)
    title=models.CharField(max_length=50,null=True)
    descriptiom=models.CharField(max_length=200,null=True)
    price=models.IntegerField()
    Discount=models.SmallIntegerField()
    image=models.ImageField(upload_to='product/image',null=True)
    body=models.TextField(null=True)
    size=models.ManyToManyField(Size,related_name='products',null=True,blank=True)
    color=models.ManyToManyField(Color,related_name='products',null=True,blank=True)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('product:detail',kwargs={'slug':self.slug})

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug=slugify(self.title)
        super().save()


class Information(models.Model):
    body=models.TextField(null=True)
    productid=models.ForeignKey(product,on_delete=models.CASCADE,related_name='info')

    def __str__(self):
        return f'{self.body}'
# Create your models here.


