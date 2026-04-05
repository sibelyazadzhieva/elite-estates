from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class AccountsTests(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(
            username='testuser',
            email='test@user.com',
            password='testpassword'
        )

    def test_login_page_loads(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_register_page_loads(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_profile_requires_login(self):
        response = self.client.get(reverse('profile_details'))
        self.assertEqual(response.status_code, 302)

    def test_profile_loads_for_logged_user(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('profile_details'))
        self.assertEqual(response.status_code, 200)

    def test_user_creation_in_db(self):
        self.assertEqual(UserModel.objects.count(), 1)
        self.assertEqual(self.user.username, 'testuser')