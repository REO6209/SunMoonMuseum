from django.db import models

from curatorapp.validators import validate_file_extension


# Create your models here.
# 상설전시관
class Permanent(models.Model):
    title = models.CharField(max_length=30, null=False)
    image = models.ImageField(upload_to='permanent/img/', null=False)
    content = models.TextField(null=True)
    mp3 = models.FileField(upload_to='permanent/mp3/', validators=[validate_file_extension])

# 성서전시관
class Bible(models.Model):
    title = models.CharField(max_length=30, null=False)
    image = models.ImageField(upload_to='bible/img/', null=False)
    content = models.TextField(null=True)
    mp3 = models.FileField(upload_to='bible/mp3/', validators=[validate_file_extension])

# 특별전시관
class Special(models.Model):
    title = models.CharField(max_length=30, null=False)
    image = models.ImageField(upload_to='special/img/', null=False)
    content = models.TextField(null=True)
    mp3 = models.FileField(upload_to='special/mp3/', validators=[validate_file_extension])