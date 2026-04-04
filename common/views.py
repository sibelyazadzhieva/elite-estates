from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .models import ContactMessage
from .forms import ContactForm

class HomeView(TemplateView):
    template_name = 'common/home.html'

class ContactView(CreateView):
    model = ContactMessage
    form_class = ContactForm
    template_name = 'common/contact.html'
    success_url = reverse_lazy('home')