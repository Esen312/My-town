from modeltranslation.translator import register, TranslationOptions
from .models import Announcement, TownHallManagement, History


@register(Announcement)
class AnnouncementTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


@register(History)
class AnnouncementTranslationOptions(TranslationOptions):
    fields = ('title', 'text')
