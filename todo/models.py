from django.db import models
from django.contrib.auth.models import User



class Todo(models.Model): 
    
   user =models.ForeignKey(User,on_delete=models.CASCADE)
   id_user=models.IntegerField(primary_key=True,default=0)
   bio=models.TextField(blank=True,default='')
   profileimg=models.ImageField(upload_to='profile_images',default='Screenshot (26).png')
   location=models.CharField(max_length=100,blank=True,default='')
   
   
   def __ste__(self):
       return self.user.username
   