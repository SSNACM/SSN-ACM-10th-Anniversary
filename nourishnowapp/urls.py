"""
URL configuration for nourishnowapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('', views.indexPage, name ="indexPage"),
    path('', views.indexPage, name ="indexPage"),
    path('signinPage/', views.signinPage, name ="signinPage"),
    path('signupDonorPage/', views.signupDonorPage, name ="signupDonorPage"),
    path('signupVolunteerPage/', views.signupVolunteerPage, name ="signupVolunteerPage"),
    path('signupAcceptorPage/', views.signupAcceptorPage, name ="signupAcceptorPage"),
    path('feedback/', views.gotoForm, name ="feedback"),
    path('postsign/', views.postsign, name ="dashboardDonorPage"),
    path('acceptor/', views.acceptor, name ="dashboardDonorPage"),
    path('donor/', views.donor, name ="dashboardDonorPage"),
    path('volunteer/', views.volunteer, name ="dashboardDonorPage"),
    path('food/', views.food, name ="dashboardDonorPage"),
    path('acceptorFood/', views.acceptorFood, name ="dashboardAcceptorPage"),
    path('pdfView', views.pdfview, name ="pdfViewer"),
    path('contactSubmit/', views.contactSubmit, name ="signupPage")
]
