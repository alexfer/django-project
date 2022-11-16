from django.urls import path
from . import views

urlpatterns = [
    path('content/<int:id>/', views.show, name='show'),
    path('accounts/content/create/', views.create, name='create-entry'),
    path('accounts/content/collection/', views.collection, name='collection-entries'),
]
