from django.db import models


class Post(models.Model):
    title       = models.CharField(max_length=45, null=False)
    content     = models.TextField(max_length=500, null=False)
    image       = models.URLField(max_length=500, null=True)
    user        = models.CharField(max_length=45, null=False)
    
    class Meta:
        db_table = "posts"