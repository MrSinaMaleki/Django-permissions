from django.db import models
from account.models import CustomUser
from django.core.validators import MinLengthValidator

# Create your models here.
# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     book_owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"Book: {self.title}"


class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_book_count(self):
        return 0


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name



class Book(models.Model):
    title = models.CharField(max_length=200, validators=[MinLengthValidator(2)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    categories = models.ManyToManyField(Category, related_name="books")
    published_date = models.DateField()


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/books/{self.title}/"

