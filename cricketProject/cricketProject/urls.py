"""cricketProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from cricketApp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.team_list_view, name='team_list'),
    url(r'^team_detail/(?P<id>\d+)/',views.team_detail_view, name='team_detail'),
    url(r'^player_detail/(?P<id>\d+)/',views.player_detail_view, name='player_detail'),
    url(r'^match_list/', views.MatchListView.as_view(), name='match_list'),
    url(r'^match_create/', views.MatchCreateView.as_view(), name='match_create'),
    url(r'^match_update/(?P<pk>\d+)/', views.MatchUpdateView.as_view(), name='match_update'),
    url(r'^match_delete/(?P<pk>\d+)/', views.MatchDeleteView.as_view(), name='match_delete'),
    url(r'^point_list/', views.point_list_view, name='point_list'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
