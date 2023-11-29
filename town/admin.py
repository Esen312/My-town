from django.contrib import admin
from django import forms
from town.form import PhotoFormSet
from town.models import Announcement, News, Feedback, Contact, OfficialDocuments, History, TownHallManagement, Photo, \
    HistoryPhoto
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
    formset = PhotoFormSet


class HistoryAdminForm(forms.ModelForm):
    text_ru = forms.CharField(label="Текст[ru] ", widget=CKEditorUploadingWidget())
    text_ky = forms.CharField(label="Текст[ky] ", widget=CKEditorUploadingWidget())

    class Meta:
        model = History
        fields = '__all__'


class HistoryModelAdmin(TranslationAdmin):
    inlines = [PhotoHistoryInline]
    form = HistoryAdminForm


admin.site.register(Announcement, AnnouncementModelAdmin)
admin.site.register(OfficialDocuments)
admin.site.register(News)
admin.site.register(Feedback)
admin.site.register(Contact)
admin.site.register(History, HistoryModelAdmin)
admin.site.register(TownHallManagement)
