from django.urls import path

from . import views

urlpatterns = [
    path('userManage/', views.userManage),
    path('userlist/', views.userlist),
    path('login/',views.login),
    path('loginHandler/',views.loginHandler),
    path('homepage/',views.homePage),
    path('menu/',views.menu),
]