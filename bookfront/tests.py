from django.test import TestCase
from datetime import date

from rest_framework.exceptions import ValidationError

from bookfront.models import Book, Author, Category

class AuthorModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Hellia")

    def test_author_name_uniqueness(self):
        """This method ensures that the name of an author is unique"""
        with self.assertRaises(Exception):
            Author.objects.create(name="Hellia")


    def test_get_book_count(self):
        self.assertEqual(self.author.get_book_count(), 0)

        Book.objects.create(author=self.author, title="Test", published_date=date(2000, 6, 26))

        self.assertEqual(self.author.get_book_count(), 1)


class BookModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Sanaz")
        self.category = Category.objects.create(name="Fantasy")

    def test_book_title_min_length(self):
        book = Book.objects.create(title="A", author=self.author, published_date=date(2000, 6, 26))
        with self.assertRaises(ValidationError):
            book.full_clean()


    def test_get_absolute_url(self):
        book = Book.objects.create(title="booktesttitle", author=self.author, published_date=date(2000, 6, 26))
        expected_url = f"/books/{book.id}/"
        self.assertEqual(book.get_absolute_url(), expected_url)


class RelationshipTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Parisa")
        self.category_fantesy = Category.objects.create(name="Fantasy1")
        self.category_advanture = Category.objects.create(name="Advanture")

        self.book = Book.objects.create(title= "Art of war", author=self.author, published_date=date(2000,3,11))

        # many to many relationship
        self.book.categories.add(self.category_fantesy, self.category_advanture)


    def test_book_author_relation(self):
        self.assertEqual(self.book.author.name, "Parisa")

    def test_book_category_relationship(self):
        self.assertEqual(self.book.categories.count(), 2)
        self.assertIn(self.category_fantesy, self.book.categories.all())
        self.assertIn(self.category_advanture, self.book.categories.all())
