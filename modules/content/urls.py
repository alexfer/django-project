from django.urls import path
from . import views
from . import account_vews

urlpatterns = [
    path('content/<slug:slug>/', views.details, name='details'),
    path('accounts/content/change/<slug:slug>/', account_vews.ChangeEntry, name='change-entry'),
    path('accounts/content/destroy/<int:id>/', account_vews.DestroyEntry, name='destroy-entry'),
    path('accounts/content/create/', account_vews.CreateEntry, name='create-entry'),
    path('accounts/content/collection/', account_vews.EntryListView.as_view(), name='collection-entries'),
    path('entries/', views.EntriesListView.as_view(), name='entries'),
]
