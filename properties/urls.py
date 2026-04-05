from django.urls import path
from .views import (
    PropertyListView, PropertyDetailView, PropertyListAPIView,
    PropertyCreateView, PropertyUpdateView, PropertyDeleteView, PropertyLikeView, FavoritePropertiesView
)

urlpatterns = [
    path('catalog/', PropertyListView.as_view(), name='property_catalog'),
    path('api/catalog/', PropertyListAPIView.as_view(), name='api_property_catalog'),
    path('add/', PropertyCreateView.as_view(), name='add_property'),
    path('<int:pk>/', PropertyDetailView.as_view(), name='property_detail'),
    path('<int:pk>/edit/', PropertyUpdateView.as_view(), name='edit_property'),
    path('<int:pk>/delete/', PropertyDeleteView.as_view(), name='delete_property'),
    path('<int:pk>/like/', PropertyLikeView.as_view(), name='like_property'),
    path('favorites/', FavoritePropertiesView.as_view(), name='favorite_properties'),
]