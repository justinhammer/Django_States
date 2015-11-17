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
    url(r'^admin/', include(admin.site.urls)),

    url(r'^ajax_state_list/$', 'main.views.ajax_state_list'),
    url(r'^api_state_list/$', 'main.views.api_state_list'),
    url(r'^ajax_city_list/$', 'main.views.ajax_city_list'),
    url(r'^api_city_list/$', 'main.views.api_city_list'),

    url(r'^state_list/$', 'main.views.state_list'),
    url(r'^state_detail/(?P<pk>\d+)/$', 'main.views.state_detail'),
    url(r'^state_search/$', 'main.views.state_search'),
    url(r'^city_search/$', 'main.views.city_search'),
    url(r'^city_detail/(?P<pk>\d+)/$', 'main.views.city_detail'),
    url(r'^city_create/$', 'main.views.city_create'),
    url(r'^state_capital_detail/(?P<pk>\d+)/$', 'main.views.state_capital_detail'),
    url(r'^city_list/$', 'main.views.city_list'),
    url(r'^state_create/$', 'main.views.state_create'),
    url(r'^contact_view/$', 'main.views.contact_view'),
    url(r'^city_edit/(?P<pk>\d+)/$', 'main.views.city_edit'),
    url(r'^state_edit/(?P<pk>\d+)/$', 'main.views.state_edit'),
    url(r'^city_create/$', 'main.views.city_create'),
    url(r'^state_search/$', 'main.views.state_create'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
