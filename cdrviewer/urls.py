"""cdrviewer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
#from cdrviewerapp.views import hello,cdtime,incalls,rates,payments,login_user,logout_user,index
from cdrviewerapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/', views.hello),
    url(r'^cdtime/', views.cdtime),
    url(r'^incalls/', views.incalls),
    url(r'^outcalls/', views.outcalls),
    url(r'^ratedcdrs/', views.ratedcdrs),
    url(r'^rates/', views.rates),
    url(r'^payments/', views.payments),
    url(r'^login/$', views.login_user, name='auth'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^index/', views.index)
]
