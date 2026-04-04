from django.views.generic import ListView, DetailView
from .models import Property
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from .serializers import PropertySerializer
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import PropertyForm

class PropertyListView(ListView):
    model = Property
    template_name = 'properties/property_list.html'
    context_object_name = 'properties'

class PropertyDetailView(DetailView):
    model = Property
    template_name = 'properties/property_detail.html'
    context_object_name = 'property'

class PropertyListAPIView(ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [AllowAny]

class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

class PropertyCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Property
    form_class = PropertyForm
    template_name = 'properties/property_form.html'
    success_url = reverse_lazy('property_catalog')

    def form_valid(self, form):
        form.instance.agent = self.request.user
        return super().form_valid(form)

class PropertyUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Property
    form_class = PropertyForm
    template_name = 'properties/property_form.html'

    def get_success_url(self):
        return reverse_lazy('property_detail', kwargs={'pk': self.object.pk})

class PropertyDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
        model = Property
        template_name = 'properties/property_confirm_delete.html'
        success_url = reverse_lazy('property_catalog')
