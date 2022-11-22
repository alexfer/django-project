from django.urls import path
from . import views

urlpatterns = [
    path('content/<slug:slug>/comment/', views.comment, name='comment'),
]
