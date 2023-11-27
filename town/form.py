from .models import News
from django.forms import ModelForm


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'date', 'text', 'image']