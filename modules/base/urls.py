from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='index'),
    path('about/', views.AboutStaticView, name='about'),
]
