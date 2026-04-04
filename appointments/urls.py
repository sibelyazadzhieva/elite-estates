from django.urls import path
from .views import AppointmentCreateView, MyAppointmentsListView, AppointmentUpdateView, AppointmentDeleteView

urlpatterns = [
    path('book/<int:pk>/', AppointmentCreateView.as_view(), name='book_appointment'),
    path('my-appointments/', MyAppointmentsListView.as_view(), name='my_appointments'),
    path('edit/<int:pk>/', AppointmentUpdateView.as_view(), name='edit_appointment'),
    path('cancel/<int:pk>/', AppointmentDeleteView.as_view(), name='cancel_appointment')
]