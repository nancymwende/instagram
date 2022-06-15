from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
import datetime as dt
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',)
    profile_photo = CloudinaryField('profile_photo')
    bio = models.TextField(max_length=100,blank=True)
    name = models.CharField(blank=True, max_length=150)
    
    def __str__(self):
        return self.name

    def update(self):
            self.save()    
        
    def delete_profile(self):
            self.delete()
            
    @classmethod
    def get_profile_by_user(cls, searched_term):
        profile = cls.objects.filter(name__icontains=searched_term)
        return profile 
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
        
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.insta_profile.save()
    
class Image(models.Model):
    picture = CloudinaryField('picture')
    image_name = models.CharField(max_length=50)
    image_caption = models.TextField(max_length= 100)
    posted_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    
    def total_likes(self):
        return self.likes.count()
        
        
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
        
    @classmethod
    def update_post(cls,id,post):
        posted = Image.objects.filter(id=id).update(post = post)
        return posted    
        
    @classmethod
    def get_images(cls):
        image = Image.objects.all()
        return image    
        
    @classmethod
    def get_image_by_id(cls):
        image = Image.objects.filter(id=Image.id)
        return image 
        
    def __str__(self):
        return self.content 
        
class Likes(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    image = models.ForeignKey(Image, related_name='posts', on_delete=models.CASCADE)

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True)
    picture = models.ImageField(upload_to='feed_images',null=True,)
    caption = models.TextField(null=True)
    likes = models.PositiveIntegerField(default=0)
@classmethod
def get_images(cls):
        images = Post.objects.all()
        return images
def __str__(self):
    return str(self.caption)


class Follow(models.Model):
    user = models.OneToOneField(User, related_name='following',on_delete = models.CASCADE)
    follower = models.ForeignKey(User, related_name='followers',on_delete = models.CASCADE)
    def __str__(self):
        return self.follower

class Comments(models.Model):
    comment = models.TextField(max_length=100,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image,on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    
    
    def save_comment(self):
        self.save()
        
    def delete_comment(self):
        self.delete()
        
    @classmethod
    def get_comment(cls):
        comment = Comments.objects.all()
        return comment        
        
        