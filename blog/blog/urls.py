"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^accounts/', include('django.contrib.auth.urls')),
    path('', views.MainPageView.as_view(), name='index'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('popular/', views.PopularView.as_view(), name='popular'),
    path('topic/addpost/', views.PostAdd.as_view(), name='addpost'),
    path('topic/<int:topic_pk>/add_comment/', views.CommentAdd.as_view(), name='addcomment'),
    path('topic/<int:pk>/hide/', views.HidePostView.as_view(), name='hidepost'),
    path('topic/<int:pk>/show/', views.ShowPostView.as_view(), name='showpost'),
    path('topic/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/myposts/', views.MyPostView.as_view(), name='myposts'),
    path('profile/mycomments/', views.MyCommentView.as_view(), name='mycomments'),
    path('admin/', admin.site.urls),
]
