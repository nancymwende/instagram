# Create your views here.
from django.shortcuts import get_object_or_404, redirect, render
from requests import post
from .models import Follow, Image,Comments,Likes,Profile,Post
from .forms import CreateUserForm,NewPostForm,CommentForm,LoginForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required



# Create your views here.
# @login_required
def index(request):
        # imports photos and save it in database
    image = Image.objects.all()
    commentform = CommentForm()
        # adding context 
    ctx = {'image':image,'commentform':commentform}
    return render(request, 'index.html',ctx)

def register(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            
            user_profile=Profile(
                user=new_user,
            )
            #user_profile.save_profile()
            
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],)
            login(request, new_user)
            return redirect('index')    
    return render(request, 'registration_form.html',{'form':form},)
    


def login(request):
    form = LoginForm()
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        
        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request,user)
            return redirect('index')
    return render(request, 'login.html',{'form':form})

    

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
    
    

def get_image_by_id(request):
    image = Post.objects.all()
    comment = Post.objects.filter().all()
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('index')
    else:
        form = NewPostForm()
    return render(request,"addpost.html", {"image":image,"comment":comment,"form": form})
    

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
    
def comment(request, post_id):
    form = CommentForm()
    current_user = request.user.profile
    image = Image.objects.get(id=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.profile = current_user
            comment.image = image
            comment.save()
        return redirect('index')
    return redirect(request, 'index.html')    
    
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
    