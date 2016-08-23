from django.shortcuts import render

# Create your views here.
# coding:utf-8
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from app.models import Person
def index(request):
    c=[1,2,5]
    return HttpResponse(c[0])
def add(re):
    a=re.GET['a']
    b=re.GET['b']
    c=a+b
    return HttpResponse(c)
def add2(re,a,b):
    c=int(a)+int(b)
    return HttpResponse(c)
def old_add2_redirect(request, a, b):
    return HttpResponseRedirect(
        reverse('add2', args=(a, b))
    )

def home(request):
    string = u"我在自强学堂学习Django，用它来建网站"
    list = ["HTML", "CSS", "jQuery", "Python", "Django"]
    dict = {'site': u'自强学堂', 'content': u'各种IT技术教程'}
    return render(request, 'home.html', {'string': string,'list':list,'dict':dict})
def adduser(req):
    name=req.GET['name']
    age=req.GET['age']
    res=Person.objects.create(name=name,age=age)
    if(res):
        return HttpResponse('ok')
    else:
        return HttpResponse('fail')

