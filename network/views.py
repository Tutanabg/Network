import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.core import serializers
from django.core.serializers import serialize
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

nw = post.objects.all()

def index(request):
	pa = post.objects.all().order_by('-date_posted')
	paginator = Paginator(pa, 10)
	
	if request.GET.get('page'):
		pa = paginator.page(request.GET.get("page"))
	else:
		pa = paginator.page(1)
	return render(request, 'network/index.html', {'posts':pa})
	
		
    

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


@csrf_exempt  
@login_required
def new_post(request):
	data = json.loads(request.body)
	po = data.get("post")
	users = set()
	users.add(request.user)
	for user in users:
			pos = post(
			post=po,
			likes=0,
			posted_by=request.user,
			)
			pos.save()
			return JsonResponse({"message": "Post sent successfully."}, status=201)
			

@login_required
def all_posts(request):
	list = post.objects.order_by("-date_posted").all()
	return JsonResponse([post.serialize() for post in list], safe=False)


@login_required
def user_followed(request):
	item = profile.objects.all()
	return JsonResponse([profile.serialize() for profile in item], safe=False)


@login_required
def all_posts_edit(request, id):
	if request.method == "GET":
		list = post.objects.get(id=id)
		return JsonResponse(list.serialize(), safe=False)
	elif request.method == "PUT":
		data = json.loads(request.body)
		if data.get(likes) is not None:
			post.likes = data[likes]
		post.save(likes)
		return HttpResponse(status=204)
	else:
		return JsonResponse({"error": "GET or PUT request required."}, status=400)


@login_required
def profileview(request, username):
	
	user = User.objects.get(username=username)
	pro = profile.objects.get(user_name = user)
	list = nw.order_by("-date_posted").filter(posted_by=user)
	paginator = Paginator(list, 10)
	if request.GET.get('page'):
		list = paginator.page(request.GET.get("page"))
	else:
		list = paginator.page(1)
	
	return render(request, 'network/profile.html', {'posts':list, 'user':user, 'profile':pro })
	
			
@login_required
def following(request):
	following = profile.objects.get(user_name=request.user).following.all()
	pa = post.objects.filter(posted_by__in=following).order_by('-date_posted')
	paginator = Paginator(pa, 10)
	
	if request.GET.get('page'):
		pa = paginator.page(request.GET.get("page"))
	else:
		pa = paginator.page(1)
	return render(request, 'network/following.html', {'posts':pa})
	
	
@login_required
@csrf_exempt
def follow_user(request):
	data = json.loads(request.body)
	user = data.get('foll')
	action = data.get('cont')
	if action == 'Follow':
		user = User.objects.get(username=user)
		prof = profile.objects.get(user_name=request.user)
		prof.following.add(user)
		prof.save()
		
		prof = profile.objects.get(user_name=user)
		prof.follower.add(request.user)
		prof.save()
		return JsonResponse({'status': 201, 'cont': "Unfollow", "follower_count": profile.follower.count}, status=201)
	else:
		user = User.objects.get(username=user)
		prof = profile.objects.get(user_name=request.user)
		prof.following.remove(user)
		prof.save()
		
		prof = profile.objects.get(user_name=user)
		prof.follower.remove(request.user)
		prof.save()
		return JsonResponse({'status': 201, 'cont': "Unfollow", "follower_count": profile.follower.count}, status=201)
            

    

	
	
	
    


@csrf_exempt
@login_required
def like_post(request):
	data = json.loads(request.body)
	post_id = data.get("id")
	new_like = data.get("likes")
	po = post.objects.get(id=post_id)
	po.likes = new_like
	po.save()
	return JsonResponse({}, status=201)
	
	
@login_required
@csrf_exempt
def edit_post(request):
	data = json.loads(request.body)
	post_id = data.get("id")
	new_post = data.get("post")
	po = post.objects.get(id=post_id)
	po.post = new_post
	po.save()
	return JsonResponse({}, status=201)
       

    




