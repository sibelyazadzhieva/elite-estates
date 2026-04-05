from django.test import TestCase
from django.urls import reverse
from .models import ContactMessage

class CommonTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'common/home.html')

    def test_contact_page_status_code(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

    def test_contact_message_creation(self):
        ContactMessage.objects.create(
            name='John Doe',
            email='john@example.com',
            message='Hello world!'
        )
        self.assertEqual(ContactMessage.objects.count(), 1)

    def test_contact_message_str(self):
        msg = ContactMessage.objects.create(
            name='Jane',
            email='jane@example.com',
            message='Test'
        )
        self.assertEqual(str(msg), 'Message from Jane')