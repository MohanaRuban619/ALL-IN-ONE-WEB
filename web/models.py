from platform import mac_ver
from django.db import models
from cloudinary.models import CloudinaryField
class Web_sites(models.Model):
    Name_Of_Site = models.CharField(max_length=200)
    Image = CloudinaryField('Image')
    Site_Link = models.CharField(max_length=200)
    Description = models.CharField(max_length=10000)


# Create your models here.
