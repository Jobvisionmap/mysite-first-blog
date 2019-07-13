from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('yamazato', views.post_yamazato, name='post_yamazato')
]
