from django.contrib import admin

from town.form import PhotoFormSet
from town.models import Announcement, News, Feedback, Contact, OfficialDocuments, History, TownHallManagement, Photo


class PhotoInline(admin.TabularInline):
    model = Photo
    formset = PhotoFormSet


class AnnouncementModelAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]


admin.site.register(Announcement, AnnouncementModelAdmin)
admin.site.register(OfficialDocuments)
admin.site.register(News)
admin.site.register(Feedback)
admin.site.register(Contact)
admin.site.register(History)
admin.site.register(TownHallManagement)
