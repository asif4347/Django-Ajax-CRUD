from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model=Book
        fields=('title','publication_date','author','pages','price','book_type')