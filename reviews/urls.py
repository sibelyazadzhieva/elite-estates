from django.urls import path
from .views import ReviewListView, ReviewCreateView, ReviewDeleteView, ReviewListAPIView, ReviewUpdateView

urlpatterns = [
    path('', ReviewListView.as_view(), name='review_list'),
    path('create/<int:property_id>/', ReviewCreateView.as_view(), name='review_create'),
    path('<int:pk>/delete/', ReviewDeleteView.as_view(), name='review_delete'),
    path('api/list/', ReviewListAPIView.as_view(), name='api_review_list'),
    path('<int:pk>/edit/', ReviewUpdateView.as_view(), name='review_edit'),
]