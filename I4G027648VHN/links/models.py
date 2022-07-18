from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from managers import ActiveLinkManager

# Create your models here.
class Link(models.Model):
    target_url = models.URLField(max_length=200)
    identifier = models.SlugField(blank=True, unique=True, max_length=20)
    description = models.CharField(max_length= 200)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)
    created_date = models.DateTimeField()
    active = models.BooleanField(default=True)
    objects = models.Manager()
    public = ActiveLinkManager()


    def __str__(self) -> str:
        return self.target_url



