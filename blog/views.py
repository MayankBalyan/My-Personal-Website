from django.contrib import messages
from django.http import request
from django.http.response import Http404, HttpResponse
from django.shortcuts import redirect, render
from blog.models import *
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
import datetime 
from django.core.mail import send_mail
import math, random
# Create your views here.
def index(request):
    week_ago = datetime.date.today() - datetime.timedelta(days = 7)
    post=Post.objects.all()
    trends = Post.objects.filter(date_time__gte = week_ago).order_by('-read')
    cat=Category.objects.all()
    params={
        'post':post,
        'trends':trends,
        'cat':cat,
        'pop_post': Post.objects.order_by('-read'),
        'recent': Post.objects.order_by('-date_time'),
    }
    
    return render(request,'index.html',params)

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['message']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, "contact.html")

def post(request,slug):
    post=Post.objects.filter(slug=slug).first()
    comments= BlogComment.objects.filter(post=post)
    context={'post':post, 'comments': comments, 'user': request.user}
    
    return render(request,'post.html',context)


def search(request):
    query=request.GET['query']
    if len(query)>78:
        allPosts=Post.objects.none()
    else:
        allPosts= Post.objects.filter(title__icontains=query)
        
        
    if allPosts.count()==0:
        messages.error(request, "No search results found. Please refine your query.")
    params={'allPosts': allPosts, 'query': query}
    return render(request, 'search.html', params)

def latestpost(request):
    post=Post.objects.order_by('-date_time')[:10]
    return render(request,'latest.html',{'post':post})

def trending(request):
    week_ago = datetime.date.today() - datetime.timedelta(days = 7)
    
    post = Post.objects.filter(date_time__gte = week_ago).order_by('-read')
    return render(request,"trending.html",{'post':post})
def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(sno=postSno)
        comment=BlogComment(comment= comment, user=user, post=post)
        comment.save()
        messages.success(request, "Your comment has been posted successfully")
        
        return redirect(f"/blog/{post.slug}")

    else:
        messages.ERROR(request,"Not Found")
        return redirect('/')


def category(request, url):
    cat = Category.objects.get(slug=url)
    posts = Post.objects.filter(category=cat)
    return render(request, "category-single.html", {'cat': cat, 'posts': posts})

def allcategory(request):
    cat=Category.objects.all()
    return render(request,'category.html',{'cat':cat})

def login_page(request):
    return render(request,'user/login-page.html')
def register_page(request):
    return render(request,'user/register-page.html')


def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
      

        # check for errorneous input
        if len(username)<10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your Account has been successfully created! NOW YOU CAN LOGIN!")
        return redirect('login')

    else:
        return HttpResponse("404 - Not found")


def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("login-page")

    return HttpResponse("404- Not found")
   

    

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')


