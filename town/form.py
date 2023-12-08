from .models import News, Photo, Announcement, NewsPhoto, HistoryPhoto, History, OfficialDocuments, \
    OfficialDocumentsPhoto, TownHallManagement, PassportOfTown, Vacancy
from django.forms import ModelForm, inlineformset_factory
from django import forms
from .models import Feedback
from ckeditor_uploader.widgets import CKEditorUploadingWidget


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


class NewsPhotoForm(forms.ModelForm):
    class Meta:
        model = NewsPhoto
        fields = ['image']


class HistoryPhotoForm(forms.ModelForm):
    class Meta:
        model = HistoryPhoto
        fields = ['image']


class OfficialDocumentsPhotoForm(forms.ModelForm):
    class Meta:
        model = OfficialDocumentsPhoto
        fields = ['image']


PhotoFormSet = inlineformset_factory(Announcement, Photo, form=PhotoForm, extra=1, can_delete=True)
NewsPhotoFormSet = inlineformset_factory(News, NewsPhoto, form=NewsPhotoForm, extra=1, can_delete=True)
HistoryPhotoFormSet = inlineformset_factory(History, HistoryPhoto, form=HistoryPhotoForm, extra=1, can_delete=True)
OfficialDocumentsFormSet = inlineformset_factory(OfficialDocuments, OfficialDocumentsPhoto,
                                                 form=OfficialDocumentsPhotoForm, extra=1, can_delete=True)


class TownHallManagementAdminForm(forms.ModelForm):
    education_ru = forms.CharField(label="Образование[ru]", widget=CKEditorUploadingWidget(), required=False)
    education_ky = forms.CharField(label="Образование[ky]", widget=CKEditorUploadingWidget(), required=False)
    work_experience_ru = forms.CharField(label="Опыт работы[ru]", widget=CKEditorUploadingWidget(), required=False)
    work_experience_ky = forms.CharField(label="Опыт работы[ky]", widget=CKEditorUploadingWidget(), required=False)

    class Meta:
        model = TownHallManagement
        fields = '__all__'


class AnnouncementAdminForm(forms.ModelForm):
    text_ru = forms.CharField(label="Текст[ru]", widget=CKEditorUploadingWidget(), required=False)
    text_ky = forms.CharField(label="Текст[ky]", widget=CKEditorUploadingWidget(), required=False)

    class Meta:
        model = Announcement
        fields = '__all__'


class HistoryAdminForm(forms.ModelForm):
    text_ru = forms.CharField(label="Текст[ru] ", widget=CKEditorUploadingWidget(), required=False)
    text_ky = forms.CharField(label="Текст[ky] ", widget=CKEditorUploadingWidget(), required=False)

    class Meta:
        model = History
        fields = '__all__'


class NewsAdminForm(forms.ModelForm):
    text_ru = forms.CharField(label="Текст[ru]", widget=CKEditorUploadingWidget(), required=False)
    text_ky = forms.CharField(label="Текст[ky]", widget=CKEditorUploadingWidget(), required=False)

    class Meta:
        model = News
        fields = '__all__'


class PassportAdminForm(forms.ModelForm):
    text_ru = forms.CharField(label="Текст паспорта[ru] ", widget=CKEditorUploadingWidget(), required=False)
    text_ky = forms.CharField(label="Текст паспорта[ky] ", widget=CKEditorUploadingWidget(), required=False)

    class Meta:
        model = PassportOfTown
        fields = '__all__'


class OfficialDocumentsAdminForm(forms.ModelForm):
    text_ru = forms.CharField(label="Текст[ru]", widget=CKEditorUploadingWidget(), required=False)
    text_ky = forms.CharField(label="Текст[ky]", widget=CKEditorUploadingWidget(), required=False)

    class Meta:
        model = OfficialDocuments
        fields = '__all__'


class VacancyAdminForm(forms.ModelForm):
    text_ru = forms.CharField(label="Текст[ru]", widget=CKEditorUploadingWidget(), required=False)
    text_ky = forms.CharField(label="Текст[ky]", widget=CKEditorUploadingWidget(), required=False)

    class Meta:
        model = Vacancy
        fields = '__all__'

class NewsFilterForm(forms.Form):
    start_date = forms.DateField(label='Начальная дата', required=False, widget=forms.TextInput(attrs={'type': 'date'}))
    end_date = forms.DateField(label='Конечная дата', required=False, widget=forms.TextInput(attrs={'type': 'date'}))


class AnnouncementFilterForm(forms.Form):
    start_date = forms.DateField(label='Начальная дата', required=False, widget=forms.TextInput(attrs={'type': 'date'}))
    end_date = forms.DateField(label='Конечная дата', required=False, widget=forms.TextInput(attrs={'type': 'date'}))


class OfficialDocumentsFilterForm(forms.Form):
    start_date = forms.DateField(label='Начальная дата', required=False, widget=forms.TextInput(attrs={'type': 'date'}))
    end_date = forms.DateField(label='Конечная дата', required=False, widget=forms.TextInput(attrs={'type': 'date'}))
