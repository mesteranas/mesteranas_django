from django import forms
from . import models
from django.utils.translation import gettext as _
class new_accound (forms.Form):
    frist_name=forms.CharField(label=_("first name"))
    last_name=forms.CharField(label=_("last name"))
    email=forms.CharField(label=_("email"),widget=forms.EmailInput())
    user_name=forms.CharField(label=_("user name"))
    password=forms.CharField(label=_("password"),min_length=8,widget=forms.PasswordInput())
    confpassword=forms.CharField(label=_("confirm password"),min_length=8,widget=forms.PasswordInput())
class login(forms.Form):
    user_name=forms.CharField(label=_("user name"))
    password=forms.CharField(label=_("password"),widget=forms.PasswordInput())
class delete(forms.Form):
    password=forms.CharField(label=_("confirm password to delete account"),widget=forms.PasswordInput())
class ChangePassword(forms.Form):
    currentPassword=forms.CharField(label=_("current password"),widget=forms.PasswordInput())
    newPassword=forms.CharField(min_length=8,label=_("new password"),widget=forms.PasswordInput())
    confNewPassword=forms.CharField(min_length=8,label=_("confirm new password"),widget=forms.PasswordInput())
class Comment(forms.Form):
    title=forms.CharField(label=_("title"))
    description=forms.CharField(label=_("content"),widget=forms.Textarea)
def getCategory():
    categories=[("all","all")]
    for post in models.post.objects.all().order_by("-date"):
        List=(post.category,post.category)
        if List in categories:
            continue
        categories.append(List)
    return categories
class SelectCategory(forms.Form):
    category=forms.ChoiceField(choices=getCategory(),label=_("select category"))
class RequestAProjectForm(forms.Form):
    describ=forms.CharField(label=_("describe your project full description"),widget=forms.Textarea)
    contect=forms.CharField(label=_("type your whatsapp phone number with your country code or your telegram username"))