# Create your views here.
from django.shortcuts import get_object_or_404, redirect, render
from .models import Follow, Image,Comments,Likes
from .forms import CreateUserForm,NewPostForm,CommentForm
from .models import Image,Profile,Likes,Comments,Follow
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User



# Create your views here.
def index(request):
        # imports photos and save it in database
    image = Image.objects.all()
    commentform = CommentForm()
    comment = Comments.objects.all()
        # adding context 
    ctx = {'image':image,'commentform':commentform,'comment':comment}
    return render(request, 'index.html',ctx)

def register(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'register.html',{'form':form})
    
def login(request):
    return render(request, 'login.html')
    

def like(request, image_id):
    user = request.user
    image = Image.objects.get(pk=image_id)
    like = Likes.objects.filter(user=user, image=image)
    if like:
        like.delete()
    else:
        new_like = Likes(user=user, image=image)
        new_like.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))    
    
    

def addPost(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('index')
    else:
        form = NewPostForm()
    return render(request, 'addPost.html', {"user":current_user,"form":form})
    

def search(request):
    if "profile" in request.GET and request.GET["profile"]:
        searched_item=request.GET["profile"]
        items= Profile.get_profile_by_user(searched_item)
        message = f"{searched_item}"


        return render(request, 'search.html',{"message":message,"items":items})
    else:
        message = "Kindly input a search term to get any results"
        return render(request, 'search.html',{"message":message})
        
def show(request):
    try:
        profiles = Profile.objects.all()
        
        context = {}
        context['profiles'] = profiles

    except:
        ValueError
        raise 'Error'
    return render(request, "search.html",context)        
    
    
    
def follow(request, user_id):
    user = request.user
    other_user = User.objects.get(id=user_id)
    follow = Follow.objects.filter(follower=user, followed=other_user)
    if follow:
        follow.delete()
    else:
        new_follow = Follow(follower=user, followed=other_user)
        new_follow.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))    