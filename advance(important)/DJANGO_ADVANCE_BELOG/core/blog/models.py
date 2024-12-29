from django.db import models
from django.contrib.auth import get_user_model


# getting user model object
User = get_user_model()

class Post(models.Model):
    '''
    this is class is define for blog app
    '''
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    images=models.ImageField(null=True, blank=True)
    title=models.CharField(max_length=250)
    id=models.AutoField(primary_key=True)
    status=models.BooleanField()
    category=models.ForeignKey('Category',null=True,on_delete=models.SET_NULL)
    
    
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    published_date=models.DateTimeField()
    
    
    def __str__(self):
        return self.title
     
class Category(models.Model):
    name=models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
         