"""blogProjects URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from blogProjects.settings import  MEDIA_ROOT
import xadmin
from django.urls import path,re_path
from django.conf.urls import url, include
from blog.views import IndexView,BlogFamilyView,BlogDetailView,blog_show_comment,search,page_not_found,server_error
# from django.views.generic import TemplateView
from django.views.static import serve
from DjangoUeditor.views import get_ueditor_controller
from django.views.generic.base import RedirectView
handler404 = page_not_found
handler500=server_error
urlpatterns = [
    url(r'^accounts/', include('allauth.urls')),
    url(r'^ueditor/', include(('DjangoUeditor.urls', 'ueditor'), namespace="ueditor")),
    url(r'^page_not_found/$', page_not_found, name='page_not_found'),
    url(r'^comments/', include('django_comments.urls')),
    path('admin/', xadmin.site.urls),

    path('',IndexView.as_view(),name='index'),
    url(r'^search/$', search, name='search'),

    path('<str:slug>', BlogFamilyView.as_view(), name='blogFamily'),

    path('<str:main_slug>/<str:son_slug>/',BlogDetailView.as_view(),name="blogDetail"),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT, }),

    url(r'^blog/(?P<id>\d+)/commentshow/$', blog_show_comment, name='showcomment'),
    # re_path(r"^ueditor/",include(('DjangoUeditor.urls','ueditor'),namespace="ueditor")),

    # url(r'^controller/$',get_ueditor_controller)
    # re_path(r'^static/(?P<path>.*)$',  serve, {"document_root":STATIC_ROOT}),





]
