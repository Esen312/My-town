from django.views.generic import ListView
from .models import Announcement


class AnnouncementListView(ListView):
    template_name = 'pages/announcement.html'
    queryset = Announcement.objects.all()
    context_object_name = 'announcements'
