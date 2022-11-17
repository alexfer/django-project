from django.urls import path
from . import views

urlpatterns = [
    path('content/<int:id>/', views.show, name='show'),
    path('accounts/content/change/<int:id>/', views.change, name='change-entry'),
    path('accounts/content/destroy/<int:id>/', views.destroy, name='destroy-entry'),
    path('accounts/content/create/', views.create, name='create-entry'),
    path('accounts/content/collection/', views.collection, name='collection-entries'),
]
