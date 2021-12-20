from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from tinymce.models import HTMLField




class Category(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField()
    img=models.ImageField(upload_to="post")
    def __str__(self):
        return self.title

# Create your models here.
class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    slug=models.SlugField()
    content=HTMLField()
    published=models.BooleanField(default=False)
    img=models.ImageField(upload_to="post")
    date=models.DateField(auto_now=True)
    date_time=models.DateTimeField(auto_now_add=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    read = models.IntegerField(default = 0)
    class Meta:
        ordering = ('-date',)
        

    def __str__(self):
        return self.title

class BlogComment(models.Model):
    sno= models.AutoField(primary_key=True)
    comment=models.TextField() 
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=now)

    def __str__(self):
        return self.user.first_name

class Contact(models.Model):
     sno= models.AutoField(primary_key=True)
     name= models.CharField(max_length=255)
     phone= models.CharField(max_length=13)
     email= models.CharField(max_length=100)
     content= models.TextField()
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)
     def __str__(self):
          return "Message from " + self.name + ' - ' + self.email


