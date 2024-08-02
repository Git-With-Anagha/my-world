from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('sample/',views.sample,name='sample'),
    path('sample1/',views.sample1,name='sample1'),
]