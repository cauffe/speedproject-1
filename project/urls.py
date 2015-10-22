"""project URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', 'main.views.list_view'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^detail_view/(?P<pk>\d+)/$', 'main.views.detail_view'),
    url(r'^list_view/$', 'main.views.list_view'),
    url(r'^create_view1/$', 'main.views.create_view1'),
    url(r'^create_view2/$', 'main.views.create_view2'),
    url(r'^update_view/(?P<pk>\d+)/$', 'main.views.update_view'),
    url(r'^delete_view/(?P<pk>\d+)/$', 'main.views.delete_view'),
    url(r'^signup/$', 'main.views.signup'),

    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^logout/$', 'main.views.logout_view'),
    #url(r'^login/$', 'main.views.login_view'),
    url(r'^login/$', 'main.views.login'),
    url(r'^vote/(?P<pk>\d+)/$', 'main.views.vote'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
