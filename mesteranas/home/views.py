import requests
from django.utils.translation import gettext_lazy as _,activate,get_language
from django.shortcuts import render,redirect,get_object_or_404
from . import forms,models
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.

def home_(r):
    activate(r.session.get('django_language', None))
    return render(r,"home.html")
def Contect(r):
    return render(r,"contect.html")
def about(r):
    return render(r,"about.html")
def changeLanguage(r):
    if r.method=="POST":
        language=r.POST["language"]
        activate(language)
        r.session['django_language'] = language
        return redirect("homePage")
    return render(r,"changeLanguage.html")
def newaccound(r):
    if r.method=="POST":
        frm=forms.new_accound(r.POST)
        if frm.is_valid():
            fristName=frm.cleaned_data["frist_name"]
            lastName=frm.cleaned_data['last_name']
            email=frm.cleaned_data["email"]
            userName=frm.cleaned_data["user_name"]
            password=frm.cleaned_data["password"]
            confpassword=frm.cleaned_data["confpassword"]
            if not User.objects.filter(username=userName).exists():
                if password==confpassword:
                    user=User.objects.create_user(userName,email,password,first_name=fristName,last_name=lastName)
                    auth.login(r,user)
                    return redirect("homePage")

    frm=forms.new_accound()
    return render(r,"new-user.html",{"form":frm})
def login(r):
    if r.method=="POST":
        frm=forms.login(r.POST)
        if frm.is_valid():
            user_name=frm.cleaned_data["user_name"]
            password=frm.cleaned_data["password"]
            user=auth.authenticate(username=user_name,password=password)
            if user:
                auth.login(r,user)
                return redirect("homePage")
    frm=forms.login()
    return render(r,"login.html",{"form":frm})
@login_required
def logout(r):
    auth.logout(r)
    return redirect("homePage")
@login_required
def settings(r):
    return render(r,"profile.html")
@login_required
def deletacc(r):
    if r.method=="POST":
        frm=forms.delete(r.POST)
        if frm.is_valid():
            password=frm.cleaned_data["password"]
            user1=User.objects.get(username=r.user)
            if user1.check_password(password):
                User.delete(user1)
                return redirect("homePage")
    frm=forms.delete()
    return render(r,"deleteAccount.html",{"form":frm})
@login_required
def changePassword(r):
    if r.method=="POST":
        frm=forms.ChangePassword(r.POST)
        if frm.is_valid():
            password=frm.cleaned_data["currentPassword"]
            newpassword=frm.cleaned_data["newPassword"]
            confnewpassword=frm.cleaned_data["confNewPassword"]
            user1=User.objects.get(username=r.user)
            if user1.check_password(password):
                if newpassword==confnewpassword:
                    user1.set_password(newpassword)
                    user1.save()
                    auth.login(r,user1)
                    return redirect("homePage")
    frm=forms.ChangePassword()
    return render(r,"change_password.html",{"form":frm})
def viewblog(r,pk):
    post=get_object_or_404(models.post,pk=pk)
    title=""
    body=""
    language=get_language()
    if language=="ar":
        title=post.arabicTitle
        body=post.arabicBody
    else:
        title=post.englishTitle
        body=post.englishBody
    post.title=title
    post.body=body

    return render(r,"post.html",{"post":post})
def blog(r):
    Posts=models.post.objects.all().order_by("-date")
    posts=[]
    title=""
    body=""
    language=get_language()
    for post in Posts:
        if language=="ar":
            title=post.arabicTitle
            body=post.arabicBody
        else:
            title=post.englishTitle
            body=post.englishBody
        post.title=title
        post.body=body
        posts.append(post)

    return render(r,"blog.html",{"posts":posts})
def myProjects(re):
    page=1
    projects=[]
    while True:
        url='https://api.github.com/users/mesteranas/repos?page={}&per_page=100'.format(page)
        r=requests.get(url)
        if not r.json():
            break
        else:
            page+=1
            projects.extend(r.json())
    return render(re,"myProjects.html",{"projects":projects})
def comments(r,pk):
    post=get_object_or_404(models.post,pk=pk)
    comments = models.Comments.objects.filter(post=post).order_by("-date")
    if r.method=="POST":
        form=forms.Comment(r.POST)
        if form.is_valid():
            comment=models.Comments()
            comment.post=post
            comment.title=form.cleaned_data["title"]
            comment.content=form.cleaned_data["description"]
            comment.user=User.objects.get(username=r.user)
            comment.save()
    form=forms.Comment()
    return render(r,"comments.html",{"comments":comments,"form":form})