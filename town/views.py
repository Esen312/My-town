from django.db.models import Q
from django.http import Http404
from django.views.generic import ListView, DetailView
from .models import News, Contact, Announcement, OfficialDocuments, History, TownHallManagement
from .form import FeedbackForm
from django.shortcuts import render, redirect
from django.contrib import messages


class NewsListView(ListView):
    model = News
    template_name = 'pages/news_list.html'
    context_object_name = 'news_list'
    ordering = ['-date']


class NewsDetailView(DetailView):
    model = News
    template_name = 'pages/news_detail.html'
    context_object_name = 'news'


def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваш отзыв успешно отправлен. Спасибо!')
            return redirect('feedback')
    else:
        form = FeedbackForm()

    return render(request, 'pages/feedback.html', {'form': form})


def contact_view(request):
    contacts = Contact.objects.all()
    return render(request, 'pages/contact.html', {'contacts': contacts})


class AnnouncementListView(ListView):
    template_name = 'pages/announcement.html'
    queryset = Announcement.objects.all()
    context_object_name = 'announcements'
    ordering = ['-date']


class AnnouncementDetailView(DetailView):
    model = Announcement
    template_name = 'pages/announcement_detail.html'
    context_object_name = 'announcement'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)

        # Проверяем значение поля publicize
        if not obj.publicize:
            raise Http404("Страница не найдена")

        return obj


class OfficialDocumentsListView(ListView):
    template_name = 'pages/official_document.html'
    queryset = OfficialDocuments.objects.all()
    context_object_name = 'official_documents'
    ordering = ['-date']


class OfficialDocumentsDetailView(DetailView):
    model = OfficialDocuments
    template_name = 'pages/official_document_detail.html'
    context_object_name = 'announcement'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)

        # Проверяем значение поля publicize
        if not obj.publicize:
            raise Http404("Страница не найдена")

        return obj


class HistoryPage(ListView):
    model = History
    template_name = 'pages/history.html'
    context_object_name = 'history'


class TownHallManagementListView(ListView):
    template_name = 'pages/management.html'
    queryset = TownHallManagement.objects.all()
    context_object_name = 'managements'


def search_view(request):
    query = request.GET.get('q')

    if query:
        # Use '__iexact' for case-insensitive search
        announcements = Announcement.objects.filter(
            Q(title__iregex=rf'.*{query}.*'))
        documents = OfficialDocuments.objects.filter(
            Q(title__iregex=rf'.*{query}.*'))
        news = News.objects.filter(title__iregex=rf'.*{query}.*')

        context = {
            'announcements': announcements,
            'documents': documents,
            'news': news,
            'query': query,
        }
        return render(request, 'pages/search_results.html', context)

    return render(request, 'pages/search_results.html', {'query': None})
