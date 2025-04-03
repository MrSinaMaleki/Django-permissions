from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny , IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from bookfront.models import Book
from bookfront.serializers import BookSerializer
from bookfront.permissions import CustomIsAuthenticatedOrReadOnly, IsOwnerOrReadOnly

class MyAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({"message": "Hello World"})

    def post(self, request):
        return Response({"message": "Only Logged-in users can perform post action."})



class ListCreateBookAPI(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [CustomIsAuthenticatedOrReadOnly]


class DetailBookAPI(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsOwnerOrReadOnly]
