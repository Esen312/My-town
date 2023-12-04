from django.contrib import admin
from django import forms
from town.form import PhotoFormSet, HistoryPhotoFormSet, NewsPhotoFormSet
from town.models import Announcement, News, Feedback, Contact, OfficialDocuments, History, TownHallManagement, Photo, \
    HistoryPhoto, NewsPhoto, PassportOfTown
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from modeltranslation.admin import TranslationAdmin


class PhotoInline(admin.TabularInline):
    model = Photo
    formset = PhotoFormSet


class AnnouncementAdminForm(forms.ModelForm):
    text_ru = forms.CharField(label="Текст[ru]", widget=CKEditorUploadingWidget())
    text_ky = forms.CharField(label="Текст[ky]", widget=CKEditorUploadingWidget())

    class Meta:
        model = Announcement
        fields = '__all__'


class AnnouncementModelAdmin(TranslationAdmin):
    inlines = [PhotoInline]
    form = AnnouncementAdminForm


class PhotoHistoryInline(admin.TabularInline):
    model = HistoryPhoto
    formset = HistoryPhotoFormSet


class HistoryAdminForm(forms.ModelForm):
    text_ru = forms.CharField(label="Текст[ru] ", widget=CKEditorUploadingWidget())
    text_ky = forms.CharField(label="Текст[ky] ", widget=CKEditorUploadingWidget())

    class Meta:
        model = History
        fields = '__all__'


class HistoryModelAdmin(TranslationAdmin):
    inlines = [PhotoHistoryInline]
    form = HistoryAdminForm


class TownHallManagementAdminForm(forms.ModelForm):
    education_ru = forms.CharField(label="Образование[ru]", widget=CKEditorUploadingWidget())
    education_ky = forms.CharField(label="Образование[ky]", widget=CKEditorUploadingWidget())
    work_experience_ru = forms.CharField(label="Опыт работы[ru]", widget=CKEditorUploadingWidget())
    work_experience_ky = forms.CharField(label="Опыт работы[ky]", widget=CKEditorUploadingWidget())

    class Meta:
        model = TownHallManagement
        fields = '__all__'


class TownHallManagementModelAdmin(TranslationAdmin):
    form = TownHallManagementAdminForm


class NewsPhotoInline(admin.TabularInline):
    model = NewsPhoto
    formset = NewsPhotoFormSet


class NewsAdminForm(forms.ModelForm):
    text_ru = forms.CharField(label="Текст[ru]", widget=CKEditorUploadingWidget())
    text_ky = forms.CharField(label="Текст[ky]", widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsModelAdmin(TranslationAdmin):
    inlines = [NewsPhotoInline]
    form = NewsAdminForm


class PassportAdminForm(forms.ModelForm):
    text_ru = forms.CharField(label="Текст паспорта[ru] ", widget=CKEditorUploadingWidget())
    text_ky = forms.CharField(label="Текст паспорта[ky] ", widget=CKEditorUploadingWidget())

    class Meta:
        model = PassportOfTown
        fields = '__all__'


class PassportModelAdmin(TranslationAdmin):
    form = PassportAdminForm


admin.site.register(Announcement, AnnouncementModelAdmin)
admin.site.register(OfficialDocuments)
admin.site.register(News, NewsModelAdmin)
admin.site.register(Feedback)
admin.site.register(Contact)
admin.site.register(History, HistoryModelAdmin)
admin.site.register(TownHallManagement, TownHallManagementModelAdmin)
admin.site.register(PassportOfTown, PassportModelAdmin)
