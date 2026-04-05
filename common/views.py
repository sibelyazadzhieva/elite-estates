import asyncio
import threading
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .models import ContactMessage
from .forms import ContactForm
from properties.models import Property


def run_async_task(coro):
    def start_loop(c):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(c)
        loop.close()

    threading.Thread(target=start_loop, args=(coro,)).start()


async def process_contact_email_async(name, email):
    print(f"\n[ASYNC TASK] 🔄 Стартиране на фонова задача: Подготовка за имейл до {email}...")
    await asyncio.sleep(5)
    print(f"[ASYNC TASK] ✅ Фоновата задача приключи: Успешно изпратен имейл до {name} ({email})!\n")


class HomeView(TemplateView):
    template_name = 'common/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_properties'] = Property.objects.order_by('-created_at')[:3]
        return context


class ContactView(CreateView):
    model = ContactMessage
    form_class = ContactForm
    template_name = 'common/contact.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')

        run_async_task(process_contact_email_async(name, email))

        return super().form_valid(form)