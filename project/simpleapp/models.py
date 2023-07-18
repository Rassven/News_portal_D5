from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse


class Article(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Name = Title
    text = models.TextField()
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, related_name='articles')
    rating = models.FloatField(validators=[MinValueValidator(0.0)], default=0)
    pub_time = models.DateTimeField(auto_now_add=True)
    # edit_time = models.DateTimeField(null=True)

    def get_absolute_url(self):
        return reverse('About_article', args=[str(self.id)])

    # def __str__(self):
    #     return f'{self.name.title()}: {self.description[:20]}'
    # class Meta:
    #     verbose_name = "Статья"
    #     verbose_name_plural = "Статьи"


# Категория, к которой будет привязываться статья
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()
