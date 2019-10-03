from django.shortcuts import render
from django.template import loader
from django.shortcuts import render, redirect, HttpResponse
from manager.models import *
import json
import math

# Create your views here.
list=''
newslist1=[]
newslist2=[]
contentlist=[]
def home(request):
    template=loader.get_template('user/home.html')
    global list
    list=menu.objects.values("name","id").all()
    left()
    context = {"menulist":list,"index":0,"news": newslist2}
    return HttpResponse(template.render(context,request))

def detail(request):
    template=loader.get_template('user/detail.html')
    print(list)
    left()
    context = {"menulist":list,"news": newslist2}
    return HttpResponse(template.render(context,request))

def subpage(request):
    template=loader.get_template('user/subpage.html')
    newscount = news.objects.filter(catid=1).all().count()
    newspage = math.ceil(newscount / 6)
    list2 = []
    num = 1
    for i in range(0, newspage):
        list2.append(num)
        num += 1
    left()
    context = {"menulist":list,"index":1,"news": newslist2,"list":list2}
    return HttpResponse(template.render(context,request))

def subpage1(request):
    template=loader.get_template('user/subpage.html')
    newscount = news.objects.filter(catid=2).all().count()
    newspage = math.ceil(newscount / 6)
    list2 = []
    num = 1
    for i in range(0, newspage):
        list2.append(num)
        num += 1
    left()
    context = {"menulist":list,"index":2,"news": newslist2,"list":list2}
    return HttpResponse(template.render(context,request))

def subpage2(request):
    template=loader.get_template('user/subpage.html')
    newscount = news.objects.filter(catid=3).all().count()
    newspage = math.ceil(newscount / 6)
    list2 = []
    num = 1
    for i in range(0, newspage):
        list2.append(num)
        num += 1
    left()
    context = {"menulist":list,"index":3,"news": newslist2,"list":list2}
    return HttpResponse(template.render(context,request))

def subajax(request):
    menuid = request.GET.get('id')
    pagenum=request.GET.get('num')
    firstpagenum=int(pagenum)*6
    lastpagenum=int(firstpagenum)+6
    newslist=news.objects.filter(catid=menuid).order_by('-registtime').all()[firstpagenum:lastpagenum]
    newscount=news.objects.filter(catid=menuid).all().count()
    newspage=math.ceil(newscount/6)
    num=1
    list=[]
    for i in range(0,newspage):
        list.append(num)
        num+=1
    print(list)
    global contentlist
    global newslist1
    contentlist=[]
    newslist1=[]
    for item in newslist:
        newsdict={"id":item.id,"title":item.title,"titlecolor":item.title_font_color,"thumb":item.thumb,"num":item.num,"registtime":datetime.timestamp(item.registtime)}
        newslist1.append(newsdict)
        print(newslist1)
        content=news_content.objects.filter(newsid=item.id).values("content","id")
        print(content)
        for item1 in content:
            contentdict={"id":item1["id"],"content":item1["content"]}
            print(contentdict)
            contentlist.append(contentdict)
    print(contentlist)
    dic={
        "news":newslist1,
        "cont":contentlist,
        "list":list,
    }
    userinfodata = json.dumps(dic)
    response = HttpResponse(userinfodata)
    response["Access-Control-Allow-Origin"] = "*"
    return response


def detailajax(request):
    newsid = request.GET.get('newsid')
    print(newsid)
    numdata=news.objects.filter(id=newsid).values("num")
    newsnum=int(numdata[0]["num"])+1
    print(newsnum)
    news.objects.filter(id=newsid).update(num=newsnum)
    detailnews = news.objects.filter(id=newsid)
    detailcont= news_content.objects.filter(id=newsid)
    for item1 in detailcont:
        contdict={"content":item1.content}
    for item in detailnews:
        newsdict={"id":item.id,"title":item.title,"titlecolor":item.title_font_color,"thumb":item.thumb,"num":item.num,"registtime":datetime.timestamp(item.registtime)}
    newsinfo={
        "news":newsdict,
        "cont":contdict,
    }
    newsinfodata = json.dumps(newsinfo)
    response = HttpResponse(newsinfodata)
    response["Access-Control-Allow-Origin"] = "*"
    return response



def homeajax(request):
    menuid = request.GET.get('id')
    newslist=news.objects.order_by('-registtime').all()[0:4]
    global contentlist
    global newslist1
    contentlist=[]
    newslist1=[]
    for item in newslist:
        newsdict={"id":item.id,"title":item.title,"titlecolor":item.title_font_color,"thumb":item.thumb,"num":item.num,"registtime":datetime.timestamp(item.registtime)}
        newslist1.append(newsdict)
        print(newslist1)
        content=news_content.objects.filter(newsid=item.id).values("content","id")
        print(content)
        for item1 in content:
            contentdict={"id":item1["id"],"content":item1["content"]}
            print(contentdict)
            contentlist.append(contentdict)
    print(contentlist)
    dic={
        "news":newslist1,
        "cont":contentlist,
    }
    userinfodata = json.dumps(dic)
    response = HttpResponse(userinfodata)
    response["Access-Control-Allow-Origin"] = "*"
    return response


def left():
    newsranklist = news.objects.order_by('-num').all()[0:5]
    global newslist2
    newslist2 = []
    num=1
    for item in newsranklist:
        if num<6:
            newsdict={"id":item.id,"title":item.title,"titlecolor":item.title_font_color,"thumb":item.thumb,"num":item.num,"registtime":datetime.timestamp(item.registtime),"index":num}
            newslist2.append(newsdict)
            num+=1