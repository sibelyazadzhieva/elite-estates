from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from .models import Property
from .forms import PropertyForm
from .serializers import PropertySerializer


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


class PropertyLikeView(LoginRequiredMixin, View):
    def post(self, request, pk):
        property = get_object_or_404(Property, pk=pk)

        if property.likes.filter(id=request.user.id).exists():
            property.likes.remove(request.user)
        else:
            property.likes.add(request.user)

        return redirect('property_detail', pk=pk)

class FavoritePropertiesView(LoginRequiredMixin, ListView):
    model = Property
    template_name = 'properties/favorites.html'
    context_object_name = 'properties'

    def get_queryset(self):
        return self.request.user.favorite_properties.all()