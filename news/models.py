from django.db import models

# Create your models here.

class Writer(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    bio = models.TextField(blank = True, null = True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Article(models.Model):
    author = models.ForeignKey(Writer, on_delete = models.CASCADE, related_name = "articles")
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