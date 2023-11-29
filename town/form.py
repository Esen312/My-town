from .models import News, Photo, Announcement
from django.forms import ModelForm, inlineformset_factory
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


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image']


PhotoFormSet = inlineformset_factory(Announcement, Photo, form=PhotoForm, extra=1, can_delete=True)
