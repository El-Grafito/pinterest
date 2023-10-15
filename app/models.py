from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'

class Category(models.Model):
    title = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

class Post(models.Model):
    title = models.CharField('Название', max_length=100)
    description = models.TextField('Описание', blank=True, null=True)
    image = models.ImageField('Фото', blank=True, null=True)
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

