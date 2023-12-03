from modeltranslation.translator import register, TranslationOptions
from .models import Announcement, TownHallManagement, History, News


@register(Announcement)
class AnnouncementTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


@register(History)
class AnnouncementTranslationOptions(TranslationOptions):
    fields = ('title', 'text')
