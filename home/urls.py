from django.urls import path
from . import views

from django.contrib.sitemaps.views import sitemap
#from .sitemaps import ProfileSitemap, CommunitySitemap, PostSitemap

sitemapURLs = ['home']

urlpatterns = [
    path('', views.home, name='home'),
]
