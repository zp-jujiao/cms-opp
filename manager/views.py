from django.template import loader
from django.shortcuts import render, redirect, HttpResponse
from django.forms import forms
from DjangoUeditor.forms import  UEditorField
from manager.models import *
import json

# Create your views here.
#管理员管理
def userManage(request):
    template=loader.get_template('manager/manage-user.html')
    context = {}
    return HttpResponse(template.render(context,request))

def regist(request):
    form=TestUEditorForm()
    return render(request,"manager/manage-user.html",{"form":form})


class TestUEditorForm(forms.Form):
    content = UEditorField('内容', width=600, height=300, toolbars="full", imagePath="static/images/", filePath="static/files/",upload_settings={"imageMaxSize":1204000},settings={})

# 登录页面渲染
def login(request):
    template=loader.get_template('manager/manage-login.html')
    context = {}
    return HttpResponse(template.render(context,request))

def loginHandler(request):
    # 接收前端提交的数据
    username = request.POST.get("username")
    password = request.POST.get("password")
    email = request.POST.get("email")
    login_list = admin.objects.values("username","password").all()
    userinfo=login_list["username"]
    print(userinfo)
    print(1234)
    if userinfo == "error":
        return HttpResponse( "登录错误")
    if userinfo:
        #     当用户名存在的时候
        if password == userinfo["password"]:
            response = HttpResponse("登陆成功", {"id": userinfo["id"]})
            response.set_cookie("id", userinfo["id"])
            return response
        return HttpResponse(returnResult(1, "密码错误"))
    return HttpResponse(returnResult(1, "用户名错误"))

def returnResult(code,mgs,data=""):
    '''
    :param code: 0代表success ！=0 代表error
    :param mgs:  返回的信息
    :param data: 返回扥数据
    :return:
    '''
    returndata1={
        "code":code,
        "mgs":mgs,
        "data":data
    }
    returndata = json.dumps(returndata1)
    return returndata

# 首页
def homePage(request):
    template = loader.get_template('manager/manage-homePage.html')
    context = {}
    return HttpResponse(template.render(context, request))

def menu(request):
    template=loader.get_template('manager/manage-menu.html')
    context = {}
    return HttpResponse(template.render(context,request))