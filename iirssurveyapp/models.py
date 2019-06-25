from django.contrib.gis.db import models

# Create your models here.
class Userloclayer(models.Model):
    location = models.PointField(null=False)

class Layer(models.Model):
    layer = models.CharField(null=False, max_length=50)

    def __str__(self):
        return self.layer
