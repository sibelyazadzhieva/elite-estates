from django.urls import path, reverse_lazy
from .views import RegisterUserView, CustomLoginView, CustomLogoutView, ProfileDetailsView, ProfileDeleteView, ProfileEditView
from django.contrib.auth.views import PasswordChangeView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', ProfileDetailsView.as_view(), name='profile_details'),
    path('profile/edit/', ProfileEditView.as_view(), name='profile_edit'),
    path('profile/delete/', ProfileDeleteView.as_view(), name='profile_delete'),
    path('password-change/', PasswordChangeView.as_view(
            template_name='accounts/password_change.html',
            success_url=reverse_lazy('profile_details')
        ), name='password_change')
]