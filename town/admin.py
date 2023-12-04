from django.contrib import admin
from town.models import Announcement, News, Feedback, Contact


admin.site.register(Announcement)
admin.site.register(News)
admin.site.register(Feedback)
admin.site.register(Contact)