from modeltranslation.translator import register, TranslationOptions
from .models import Announcement, TownHallManagement, History, News, Contact


@register(Announcement)
class AnnouncementTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


@register(History)
class HistoryTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


@register(News)
class HistoryTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


@register(TownHallManagement)
class TownHallManagementTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name', 'middle_name', 'position', 'education', 'work_experience')