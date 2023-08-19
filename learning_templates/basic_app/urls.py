from django.contrib import admin
from django.urls import path, include
from basic_app import views

# FOR TEMPLATE TAGGING app_name is important


app_name = 'basic_app'
urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),

]
