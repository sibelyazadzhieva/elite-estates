from django.test import TestCase
from django.urls import reverse
from .models import Property
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class PropertyTests(TestCase):
    def setUp(self):
        self.agent = UserModel.objects.create_user(
            username='testagent',
            email='test@agent.com',
            password='testpassword'
        )
        self.agent.is_staff = True
        self.agent.save()

        self.property = Property.objects.create(
            title='Test Property',
            description='Test Description',
            price=100000,
            property_type='house',
            location='Test Location',
            agent=self.agent
        )

    def test_property_creation(self):
        self.assertEqual(Property.objects.count(), 1)
        self.assertEqual(self.property.title, 'Test Property')

    def test_property_catalog_view(self):
        response = self.client.get(reverse('property_catalog'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Property')

    def test_property_detail_view(self):
        response = self.client.get(reverse('property_detail', args=[self.property.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Description')

    def test_add_property_requires_login(self):
        response = self.client.get(reverse('add_property'))
        self.assertEqual(response.status_code, 302)

    def test_add_property_as_staff(self):
        self.client.login(username='testagent', password='testpassword')
        response = self.client.get(reverse('add_property'))
        self.assertEqual(response.status_code, 200)