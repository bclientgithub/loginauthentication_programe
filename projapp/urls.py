
"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('regTask',views.regTask),
    path('login',views.login),
    path('loginTask',views.loginTask),
    path('student',views.student),
    path('faculty',views.faculty),
    path('ragistration',views.ragistration),
    path('ragistration2',views.ragistration2),
    path('facultytask',views.facultytask),
    path('delete',views.delete),
    path('update',views.update),
    path('contact',views.contact),
    path('forget',views.forget),
    path('forgettask',views.forgettask),
    # path('admin',views.admin)

]