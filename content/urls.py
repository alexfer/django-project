from django.urls import path
from . import views

urlpatterns = [
    path('content/<int:id>/', views.show, name='show'),
]
