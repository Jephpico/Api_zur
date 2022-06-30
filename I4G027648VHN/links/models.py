from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.
class Link(models.Model):
    target_url = models.URLField()
    identifier = models.SlugField(blank=True, unique=True)
    description = models.CharField(max_length= 200)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)
    created_date = models.DateTimeField()
    active = models.BooleanField(default=True)


    def __str__(self) -> str:
        return self.target_url


