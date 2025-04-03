from django.db import models

from account.models import CustomUser


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    book_owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"Book: {self.title}"

