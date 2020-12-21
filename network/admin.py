from django.contrib import admin
from .models import User, post, profile
# Register your models here.
admin.site.register(User) 
admin.site.register(post) 
admin.site.register(profile) 


