from django import forms
from django.utils.translation import gettext as _
class new_accound (forms.Form):
    frist_name=forms.CharField(label=_("frist name"))
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
