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

class Reviews(models.Model):
    REVIEW_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )
    design = models.IntegerField(choices=REVIEW_CHOICES,default=0,blank=False)
    usability = models.IntegerField(choices=REVIEW_CHOICES,default=0,blank=False)
    content = models.IntegerField(choices=REVIEW_CHOICES,default=0,blank=False)
    average =  models.DecimalField(default=1,blank=False,decimal_places=2,max_digits=100)
    project = models.ForeignKey(Project,null=True,on_delete=models.CASCADE)
    user = models.ForeignKey(User,null=True,blank=True)






