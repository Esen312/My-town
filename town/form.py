from .models import News
from django.forms import ModelForm
from django import forms
from .models import Feedback


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'date', 'text', 'image']


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['first_name', 'last_name', 'contact_number', 'email', 'message', 'attachment']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Введите ваше имя'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Введите вашу фамилию'}),
            'contact_number': forms.TextInput(attrs={'placeholder': 'Введите контактный номер'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Введите ваш email'}),
            'message': forms.Textarea(attrs={'placeholder': 'Введите ваше сообщение'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['attachment'].widget.attrs.update({'accept': 'application/pdf, image/*'})


