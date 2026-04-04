from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from .models import Appointment
from .forms import AppointmentForm
from properties.models import Property
from django.views.generic import ListView, UpdateView, DeleteView

class AppointmentCreateView(LoginRequiredMixin, CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointments/book_appointment.html'

    def form_valid(self, form):
        form.instance.client = self.request.user
        form.instance.property_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('property_detail', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['property'] = get_object_or_404(Property, pk=self.kwargs['pk'])
        return context

class MyAppointmentsListView(LoginRequiredMixin, ListView):
    model = Appointment
    template_name = 'appointments/my_appointments.html'
    context_object_name = 'appointments'

    def get_queryset(self):
        return Appointment.objects.filter(client=self.request.user).order_by('date_and_time')

class AppointmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointments/appointment_update.html'
    success_url = reverse_lazy('my_appointments')

    def get_queryset(self):
        return Appointment.objects.filter(client=self.request.user)

class AppointmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Appointment
    template_name = 'appointments/appointment_confirm_delete.html'
    success_url = reverse_lazy('my_appointments')

    def get_queryset(self):
        return Appointment.objects.filter(client=self.request.user)