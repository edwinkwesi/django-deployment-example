from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Create and inherents aspect of the model class with userdefined optional object field

class UserProfileInfo(models.Model):
    
    # assign user variable to the model User class 
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    
    #create additional objects fields for User class
    portfolio_site =  models.URLField(blank=True)
    
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    
    def __str__(self):
        return self.user.username
     
    
     