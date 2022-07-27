from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    profile = models.ImageField(default='img/user.png',upload_to='img')
    address = models.CharField(max_length=120)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    is_doctor = models.BooleanField(default=False)
    is_patients = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Category(models.Model):
    cat_name = models.CharField(max_length=40)

    def __str__(self):
        return self.cat_name 

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class DoctoBlog(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='blog_img')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    summary = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    status = models.IntegerField(choices=STATUS,default=0)

    def __str__(self):
        return self.title

    