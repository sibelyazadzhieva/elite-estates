from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from properties.models import Property
from .models import Review
from .serializers import ReviewSerializer

UserModel = get_user_model()


class ReviewTests(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(
            username='testuser',
            password='testpassword123',
            email='test@example.com'
        )

        self.agent = UserModel.objects.create_user(
            username='agentuser',
            password='agentpassword123',
            email='agent@example.com'
        )

        self.property = Property.objects.create(
            title='Luxury Villa Monaco',
            price=5000000,
            description='A beautiful villa by the sea.',
            location='Monaco',
            agent=self.agent
        )

        self.review = Review.objects.create(
            property=self.property,
            author=self.user,
            rating=5,
            comment='Absolutely stunning property!'
        )

    def test_review_creation(self):
        self.assertEqual(Review.objects.count(), 1)
        self.assertEqual(self.review.rating, 5)
        self.assertEqual(self.review.author.username, 'testuser')

    def test_review_str_method(self):
        expected_str = f"Review by testuser for Luxury Villa Monaco"
        self.assertEqual(str(self.review), expected_str)

    def test_review_list_view_status_code(self):
        response = self.client.get(reverse('review_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/review_list.html')

    def test_review_list_view_search(self):
        response = self.client.get(reverse('review_list'), {'query': 'stunning'})
        self.assertContains(response, 'Absolutely stunning property!')

    def test_review_serializer(self):
        serializer = ReviewSerializer(instance=self.review)
        data = serializer.data
        self.assertEqual(data['rating'], 5)
        self.assertEqual(data['author_name'], 'testuser')
        self.assertEqual(data['property_title'], 'Luxury Villa Monaco')