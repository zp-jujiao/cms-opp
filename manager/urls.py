from django.urls import path

from . import views

urlpatterns = [
    path('userManage/', views.userManage),
    path('regist/', views.regist),
    path('login/',views.login),
    path('loginHandler/',views.loginHandler),
    path('homepage/',views.homePage),
    path('menulist/',views.menulist),
    path('addmenu/',views.addmenu),
    # path('addmenuajax/',views.addmenuajax),
]