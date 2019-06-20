from django.contrib.gis.db import models

# Create your models here.
class Userloclayer(models.Model):
    location = models.PointField(null=False)
