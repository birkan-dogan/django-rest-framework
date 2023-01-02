from django.db import models

# Create your models here.

class Article(models.Model):
    author = models.CharField(max_length = 50)
    title = models.CharField(max_length = 120)
    description = models.CharField(max_length = 200)
    text = models.TextField()
    city = models.CharField(max_length = 100)
    published_date = models.DateField()
    is_active = models.BooleanField(default = True)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"