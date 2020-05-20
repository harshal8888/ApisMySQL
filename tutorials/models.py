from django.db import models

# Create your models here.
from django.db import models


class Tutorial(models.Model):
    question = models.CharField(max_length=200, blank=False, default='')
    