from modeltranslation.translator import register, TranslationOptions
from .models import Announcement, TownHallManagement, History, News, PassportOfTown, OfficialDocuments, Vacancy


@register(Announcement)
class AnnouncementTranslationOptions(TranslationOptions):
    fields = ('title', 'text', 'file',)


@register(OfficialDocuments)
class OfficialDocumentsTranslationOptions(TranslationOptions):
    fields = ('title', 'text', 'file',)


@register(History)
class HistoryTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)


@register(News)
class HistoryTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)


@register(TownHallManagement)
class TownHallManagementTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name', 'middle_name', 'position', 'education', 'work_experience',)


@register(PassportOfTown)
class PassportOfTownTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)


@register(Vacancy)
class VacancyTranslationOptions(TranslationOptions):
    fields = ('text', 'file',)

