from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.serializers import serialize


class User(AbstractUser):
    pass
    
    
class post(models.Model): 
   post = models.CharField(max_length=100) 
   date_posted = models.DateTimeField(auto_now_add=True) 
   likes = models.IntegerField(default=0)
   posted_by = models.ForeignKey(User, on_delete=models.CASCADE, default=User.username)
      
   def serialize(self):
        return {
            "id": self.id,
            "post": self.post,
            "date_posted": self.date_posted.strftime("%b %-d %Y, %-I:%M %p"),
            "likes": self.likes,
            
        }
        
       
class profile(models.Model):
	user_name = models.ForeignKey(User, on_delete=models.CASCADE)
	follower = models.ManyToManyField(User,  blank=True, related_name="follower_user")
	following = models.ManyToManyField(User,  blank=True, related_name="following_user")
	def serialize(self):
		return {
		  "id": self.id,
		}
	
	



