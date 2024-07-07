from django.test import TestCase
from .models import Book
from datetime import date
from rest_framework.test import APIClient
from django.contrib.auth.models import User


class BookListViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/api/books/')
        self.assertEqual(resp.status_code, 200)


class BookModelTest(TestCase):
    def test_string_representation(self):
        book = Book(title="1984", author="George Orwell", publication=date.today())
        self.assertEqual(str(book), book.title)

    def test_book_creation(self):
        book = Book.objects.create(
            title="1984",
            author="George Orwell",
            publication=date(1949, 6, 8)
        )
        self.assertTrue(isinstance(book, Book))
        self.assertEqual(book.__str__(), book.title)
