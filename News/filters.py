from django_filters import FilterSet, DateFilter
from django import forms
from .models import Post


# Создаем свой набор фильтров для модели Post.
class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {

            'title': ['contains'],
            'text': ['exact'],
            'creation_time': ['gt'],
            'type': ['exact'],
            'author': ['exact'],
        }
