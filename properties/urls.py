from django.urls import path
from .views import PropertyListView, PropertyDetailView

urlpatterns = [
    path('catalog/', PropertyListView.as_view(), name='property_catalog'),
    path('<int:pk>/', PropertyDetailView.as_view(), name='property_detail')
]