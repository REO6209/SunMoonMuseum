from django.db import models

# Create your models here.
class Introduction_history(models.Model):
    date = models.CharField(max_length=20, null=False)
    content = models.TextField(null=False)