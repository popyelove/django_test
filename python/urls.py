"""python URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app import views as app_views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',app_views.index),
    url(r'^add/$',app_views.add),
    url(r'^add2/(\d+)/(\d+)/$',app_views.old_add2_redirect),
    url(r'^new_add/(\d+)/(\d+)/$', app_views.add2, name='add2'),
    url(r'^home/$', app_views.home, name='home'),
    url(r'^adduser/$',app_views.adduser, name='adduer'),


]
