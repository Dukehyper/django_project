from django.db import models

# Create your models here.
class Banner(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.title