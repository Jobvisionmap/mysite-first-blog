from django.urls import path
from . import views

urlpatterns = [
    path('blog/yamazato', views.post_yamazato, name='post_yamazato'),
    path('blog', views.post_list, name='post_list'),
    path('', views.post_list, name='post_list'),
    
]
