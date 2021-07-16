from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    profile_picture = CloudinaryField('image')
    profile_bio = models.TextField()
    profile_contact = models.CharField(max_length=60,blank=True)


class Project(models.Model):
    project_title = models.CharField(max_length=60,blank=True)
    project_image = CloudinaryField('image')
    project_description = models.TextField()
    project_link = models.URLField(blank=True)
    user = models.ForeignKey(User, null=True)
    profile = models.ForeignKey(Profile,null=True,on_delete=models.CASCADE)




