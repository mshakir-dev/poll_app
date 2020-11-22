from django.urls import path

from . import views

# There is a index method in the views.py which is calling here in the urls.py 
urlpatterns = [
  path('', views.index, name='index')
]