# Create your views here.
from django.shortcuts import get_object_or_404, redirect, render
from .models import Image
from .forms import CreateUserForm,NewPostForm
from .models import Image,Profile,Likes
from django.http import HttpResponseRedirect
from django.urls import reverse



# Create your views here.
def index(request):
        # imports photos and save it in database
    image = Image.objects.all()
        # adding context 
    ctx = {'image':image}
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