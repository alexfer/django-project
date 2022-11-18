from django.urls import path
from . import views

urlpatterns = [
    path('content/<int:id>/', views.details, name='details'),
    path('accounts/content/change/<int:id>/', views.ChangeEntry, name='change-entry'),
    path('accounts/content/destroy/<int:id>/', views.destroy, name='destroy-entry'),
    path('accounts/content/create/', views.CreateEntry, name='create-entry'),
    path('accounts/content/collection/', views.collection, name='collection-entries'),
]
