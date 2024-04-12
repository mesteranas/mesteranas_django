from django.urls import path
from . import views
urlpatterns=[
    path("",views.home_,name="homePage"),
    path("contect/",views.Contect,name="contect"),
    path("about/",views.about,name="about"),
    path("changeLanguage",views.changeLanguage,name="changeLanguage"),
    path("accounts/new",views.newaccound,name="newaccound"),
    path("accounts/login",views.login,name="login"),
    path("accounts/logout",views.logout,name="logout"),
 path("accounts/settings",views.settings,name="accountSettings")   ,
 path("accounts/delete",views.deletacc,name="deleteaccount"),
 path("accounts/changePassword",views.changePassword,name="changePassword"),
    path("blog/category/<str:category>",views.blog,name="blog"),
    path("blog/post/<int:pk>",views.viewblog,name="ViewPost"),
    path("myProjects",views.myProjects,name="myProjects"),
    path("vlog/post/<int:pk>/comments",views.comments,name="comments")
]