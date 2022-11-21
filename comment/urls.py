from django.urls import path
from . import views

urlpatterns = [
    path('content/<int:id>/comment/', views.comment, name='comment'),
]
