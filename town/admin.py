from django.contrib import admin
from town.form import (PhotoFormSet, HistoryPhotoFormSet, NewsPhotoFormSet, OfficialDocumentsFormSet,
                       AnnouncementAdminForm, HistoryAdminForm, TownHallManagementAdminForm, NewsAdminForm,
                       PassportAdminForm, OfficialDocumentsAdminForm)
from town.models import (Announcement, News, Feedback, Contact, OfficialDocuments, History, TownHallManagement, Photo,
                         HistoryPhoto, NewsPhoto, PassportOfTown, OfficialDocumentsPhoto)
from modeltranslation.admin import TranslationAdmin
from django.utils.html import format_html
from django.contrib.admin import AdminSite


AdminSite.site_header = 'Администрирование сайта мэрии г. Токмок'


class PhotoInline(admin.TabularInline):
    model = Photo
    formset = PhotoFormSet
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return format_html(f'<img src="{obj.image.url}" width="250" height="150"/>')

    get_image.short_description = "Фото"


class PhotoHistoryInline(admin.TabularInline):
    model = HistoryPhoto
    formset = HistoryPhotoFormSet
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return format_html(f'<img src="{obj.image.url}" width="250" height="150"/>')

    get_image.short_description = "Фото"


class HistoryModelAdmin(TranslationAdmin):
    inlines = [PhotoHistoryInline]
    form = HistoryAdminForm


class NewsPhotoInline(admin.TabularInline):
    model = NewsPhoto
    formset = NewsPhotoFormSet
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return format_html(f'<img src="{obj.image.url}" width="250" height="150"/>')

    get_image.short_description = "Фото"


class PassportModelAdmin(TranslationAdmin):
    form = PassportAdminForm


class OfficialDocumentsPhotoInline(admin.TabularInline):
    model = OfficialDocumentsPhoto
    formset = OfficialDocumentsFormSet
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return format_html(f'<img src="{obj.image.url}" width="250" height="150"/>')

    get_image.short_description = "Фото"


@admin.register(Announcement)
class AnnouncementAdmin(TranslationAdmin):
    list_display = ('title', 'date', 'publicize')
    search_fields = ['title']
    readonly_fields = ('get_photos',)
    form = AnnouncementAdminForm
    inlines = [PhotoInline]


@admin.register(OfficialDocuments)
class OfficialDocumentsAdmin(TranslationAdmin):
    list_display = ('title', 'date', 'publicize')
    search_fields = ['title']
    inlines = [OfficialDocumentsPhotoInline]
    form = OfficialDocumentsAdminForm


@admin.register(News)
class NewsAdmin(TranslationAdmin):
    list_display = ('title', 'date')
    search_fields = ['title']
    inlines = [NewsPhotoInline]
    form = NewsAdminForm


@admin.register(TownHallManagement)
class TownHallManagementAdmin(TranslationAdmin):
    list_display = ('position', 'first_name', 'middle_name', 'last_name', 'get_image')
    form = TownHallManagementAdminForm

    def get_image(self, obj):
        return format_html(f'<img src="{obj.image.url}" width="120" height="200" />')

    get_image.short_description = "Фото"


admin.site.register(Feedback)
admin.site.register(Contact)
admin.site.register(History, HistoryModelAdmin)
admin.site.register(PassportOfTown, PassportModelAdmin)
