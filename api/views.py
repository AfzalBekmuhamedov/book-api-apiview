from django.http import JsonResponse
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Book

@api_view(["GET","POST"])
def book_list(request):
    if request.method == "GET":
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    else:
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "created"})
        return Response({"message": "error"})

@api_view(["GET","PUT","PATCH","DELETE"])
def book_detail(request,pk):
    if request.method == "GET":
        try:
            book = Book.objects.get(pk=pk)
        except:
            return Response({"message": "Book Not Found"})
        serializer = BookSerializer(book)
        return Response(serializer.data)
    elif request.method =="PUT":
        try:
            book = Book.objects.get(pk=pk)
        except:
            return Response({"message": "Book Not Found"})
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Updated"})
        return Response({"message": "error"})
    elif request.method == "PATCH":
        try:
            book = Book.objects.get(pk=pk)
        except:
            return Response({"message": "Book Not Found"})
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Updated"})
        return Response({"message": "error"})
    elif request.method =="DELETE":
        try:
            book = Book.objects.get(pk=pk)
        except:
            return Response({"message": "Book Not Found"})
        book.delete()
        return Response({"message": "Deleted"})




