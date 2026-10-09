from django.urls import path
from api.views import *


urlpatterns = [
    path("books/", book_list,name="books"),
    path("books/<int:pk>/", book_detail, name="books"),
]