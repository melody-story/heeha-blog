from typing import ClassVar, Tuple
from django.db import models
from django.db.models.fields.files import ImageField


class Post(models.Model):
        
    title       = models.CharField(max_length=45, null=False)
    content     = models.TextField(max_length=500, null=False)
    image       = models.URLField(max_length=500, null=True)
    user        = models.CharField(max_length=45, null=False)
    create_at   = models.DateTimeField(auto_now=False, auto_now_add=True, null=False)
    modified_at = models.DateTimeField(auto_now=False, auto_now_add=True, null=False)   
    
    class Meta:
        db_table = "posts"
        
# class User(models.Mode):
#     nickname = models.CharField(max_length=50, null=False)
#     email    = models.EmailField(max_length=50, null=False)
#     password = models.CharField(max_length=50, null=False) 