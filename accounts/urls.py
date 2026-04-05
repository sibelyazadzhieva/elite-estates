from django.urls import path
from .views import RegisterUserView, CustomLoginView, CustomLogoutView, ProfileDetailsView, ProfileDeleteView, ProfileEditView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', ProfileDetailsView.as_view(), name='profile_details'),
    path('profile/edit/', ProfileEditView.as_view(), name='profile_edit'),
    path('profile/delete/', ProfileDeleteView.as_view(), name='profile_delete'),
]