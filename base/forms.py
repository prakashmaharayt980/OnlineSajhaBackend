# forms.py
from django import forms
from .models import NewsData, PostImage, AdsImage

class NewsForm(forms.ModelForm):
    class Meta:
        model = NewsData
        fields = ['title', 'description', 'type_of_news', 'post_by']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }

class PostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ['image']

class AdsImageForm(forms.ModelForm):
    class Meta:
        model = AdsImage
        fields = ['image']
