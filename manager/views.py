from django.template import loader
from django.shortcuts import render, redirect, HttpResponse
from django.forms import forms
from DjangoUeditor.forms import  UEditorField
from manager.models import *
import json
from datetime import datetime

# Create your views here.
userinfolist=[]

#管理员管理
def userManage(request):
    template=loader.get_template('manager/manage-user.html')
    form = TestUEditorForm()
    if request.method == "POST":
        headImg = request.FILES.get("headimg")
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get("email")
        print(username,password,email)
        userjub=admin.objects.filter(username=username).values("id")
        num=0
        for i in userjub:
            if i["id"] :
                num+=1
        print(headImg,123)
        if headImg!=None:
            size=headImg.size/1024
            if float(size) > 100:
                print("文件过大")
            if headImg.name.split(".")[-1] not in ["jpg", "jpeg", "png"]:
                print("文件类型不正确")
            filename = "headImg_" + str(int(datetime.now().timestamp() * 1000000)) + "." + headImg.name.split("/")[-1]
            if num == 0:
                if email != "":
                    print(123)
                    # userinfo = admin(username=username, password=password, email=email, headimg=filename)
                    # userdetail
                    # userinfo.save()
                    dic = transdata(0, "success")
            else:
                dic = transdata(1, "usererro")

            savePath = "static/uploads/" + filename
            with open(savePath, 'wb') as f:
                for file in headImg.chunks():
                    f.write(file)
                    f.flush()
        else:
            if num == 0:
                if email != "":
                    # userinfo = admin(username=username, password=password, email=email)
                    # userdetail
                    # userinfo.save()
                    dic = transdata(0, "success")
            else:
                dic = transdata(1, "usererro")
        data = json.dumps(dic)
        return HttpResponse(data)
    # username=request.
    context = {"form":form}
    return HttpResponse(template.render(context,request))

def userlist(request):
    userinfo=admin.objects.all()
    global userinfolist
    userinfolist=[]
    for item in userinfo:
        userinfodict={"id":item.id,"username":item.username,"password":item.password,"email":item.email,"headimg":item.headimg,"lasttime":item.lasttime}
        userinfolist.append(userinfodict)
    print(userinfolist)
    return render(request,"manager/manage-userlist.html",{"list":userinfolist})


class TestUEditorForm(forms.Form):
    content = UEditorField('用户详情', width=600, height=300, toolbars="full", imagePath="static/images/", filePath="static/files/",upload_settings={"imageMaxSize":1204000},settings={})

# 登录页面渲染
def login(request):
    template=loader.get_template('manager/manage-login.html')
    context = {}
    return HttpResponse(template.render(context,request))

def loginHandler(request):
    # 接收前端提交的数据
    username = request.POST.get("username")
    password = request.POST.get("password")
<<<<<<< HEAD
    login_list = admin.objects.values("username","password").all()
    userinfo=login_list["username"]
    print(userinfo)
    print(1234)
    if userinfo == "error":
        return HttpResponse( "登录错误")
=======
    email = request.POST.get("email")
    now=datetime.now()
    userinfo = admin.objects.get(username=username)
>>>>>>> 77b0e4e7678b103d2144721c9d8d0e69e7d23d96
    if userinfo:
        #     当用户名存在的时候
        if password == userinfo.password:
            admin.objects.filter(username=username).update(lasttime=datetime.now())
            response = HttpResponse(returnResult(0, "登录成功,欢迎来到路赞后台管理系统",{"id": userinfo.id}) )
            response.set_cookie("id", userinfo.id,max_age=60*60*24*1)
            return response
        return HttpResponse(returnResult(1, "密码输入错误，请重新输入"))
    return HttpResponse(returnResult(1, "用户名输入错误，请再次确认"))


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
    id = request.COOKIES["id"]
    # 登陆用户数量
    today=datetime.now().strftime("%y-%m-%d")
    userSum=admin.objects.filter(lasttime__contains=today).count()
    global name
    name = admin.objects.values("username").get(id=id)
    context = {
        "name": name,
        "userSum":userSum
    }
    return HttpResponse(template.render(context, request))

<<<<<<< HEAD
def menu(request):
    template=loader.get_template('manager/manage-menu.html')
    context = {}
    return HttpResponse(template.render(context,request))


def transdata(code, msg, id=""):
    if id == "":
        print(123)
        dic = {
            "code": code,
            "msg": msg
        }
    else:
        print(456)
        dic = {
            "code": code,
            "msg": msg,
            "id": id
        }
    return dic
=======
def menulist(request):
    template=loader.get_template('manager/manage-menulist.html')
    menuList=menu.objects.all()
    listinfo=[]
    for item in menuList:
        listinfo.append(item)
    context = {
        "listinfo":listinfo,
        # "name":name
    }
    return HttpResponse(template.render(context,request))
# 添加菜单
def addmenu(request):
    template=loader.get_template('manager/manage-addmenu.html')
    context = {
        # "name":name
    }
    return HttpResponse(template.render(context,request))


def addmenuajax(request):
    menuname =request.POST.get('menuname')
    modelname =request.POST.get('modelname')
    type = request.POST.get('position')
    open =request.POST.get('off')
    addTime = menu(name=menuname)
    addTime.save()

    return HttpResponse(0)
>>>>>>> 77b0e4e7678b103d2144721c9d8d0e69e7d23d96
