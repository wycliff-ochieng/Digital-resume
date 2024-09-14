from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User 
#from ckeditor.fields import RichTextField

class Skills(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    score = models.IntegerField(default=80,blank=True,null=True)
    image = models.FileField(blank=True,null=True,upload_to='media')
    is_it_key = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100,blank=True,null=True)
    avatar = models.ImageField(blank=True,null=True,upload_to='avatar')
    bio = models.CharField(max_length=100,blank=True,null=True)
    skills = models.ManyToManyField(Skills,blank=True)
    CV = models.FileField(blank=True,null=True,upload_to='cv')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class ContactProfile(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f'{self.name}'

class Portfolio(models.Model):
    name = models.CharField(max_length=100, blank=True,null=True)
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=True,null=True)
    slug = models.SlugField(blank=True,null=True)
    image = models.ImageField(blank=True,null=True,upload_to='portfolio')
    is_active = models.BooleanField(default=True)

    def save (self,*args,**kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Portfolio,self).save(*args,**kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/portfolio/{self.slug}"


class Blog(models.Model):
    name = models.CharField(max_length=100, blank=True,null=True)
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=True,null=True)
    slug = models.SlugField(blank=True,null=True)
    image = models.ImageField(blank=True,null=True,upload_to='blog')
    is_active = models.BooleanField(default=True)

    def save(self,*args,**kwargs):
        if not self.id:
            self.slug = slugify(self.name)
            super(Blog,self).save(*args,**kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/blog/{self.slug}"

class Certificate(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    thumbnail = models.ImageField(blank=True,null=True, upload_to='testimonials')
    name = models.CharField(max_length=100,blank=True,null=True)
    role = models.CharField(max_length=100,blank=True,null=True)
    quote = models.TextField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Media(models.Model):
    image = models.ImageField(blank=True,null=True, upload_to='media')
    url = models.URLField(blank=True,null=True)
    name = models.CharField(max_length=100,blank=True,null=True)
    is_image = models.BooleanField(default=False)

    def save(self,*args,**kwargs):
        if self.url:
            self.is_image = False
        super(self,Media).save(*args,**kwargs)

    def __str__(self):
        return self.name


