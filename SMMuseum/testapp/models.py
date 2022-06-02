from django.db import models

# Create your models here.
class TestOCR(models.Model):
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='test/', null=False)