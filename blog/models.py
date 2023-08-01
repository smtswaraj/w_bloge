from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200, default='', blank=True)
    by = models.CharField(max_length=200, default='', blank=True)
    date = models.DateField(default='', blank=True)
    articlePageImage = models.ImageField(upload_to='blog/images/', default='', blank=True)
    articlePageContent = models.TextField(default='', blank=True)
    articlePageImage2 = models.ImageField(upload_to='blog/images/', default='', blank=True)
    articlePageContent2 = models.TextField(default='', blank=True)
    articlePageImage3 = models.ImageField(upload_to='blog/images/', default='', blank=True)
    articlePageContent3 = models.TextField(default='', blank=True)

