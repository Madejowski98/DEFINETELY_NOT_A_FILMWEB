from django import forms
from .models import Movie, Review, Article, Genre


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ["title", "genre", "release_year", "director", "description", "photo"]
        # photo = forms.ImageField(required=True)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["rating", "review"]


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "description"]


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ["name"]
