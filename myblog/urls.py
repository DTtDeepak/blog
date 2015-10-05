"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from apps.blog.views import *
from allauth.urls import *
handler500 = 'apps.blog.views.error500'
# handler404 = 'apps.blog.views.error404'
urlpatterns = [
    url(r'^$', home),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^addpost/$', addPost),
    url(r'^posts/$', posts),
    url(r'^tags/$', tags),
    url(r'^posts/(?P<url>.+)/', post),
    url(r'^tags/(?P<name>.+)/$', tag),
    url(r'^search/$', search),
    url(r'^comment/', comment, name='comment'),
    url(r'^reply/', reply, name='reply'),
    url(r'^submitpost/', submitPost, name='submitpost'),
    
]
