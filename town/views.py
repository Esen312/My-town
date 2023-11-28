from django.http import Http404
from django.views.generic import ListView, DetailView
from .models import News, Contact, Announcement
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


class AnnouncementDetailView(DetailView):
    model = Announcement
    template_name = 'pages/announcement_detail_kg.html'
    context_object_name = 'announcement'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)

        # Проверяем значение поля publicize
        if not obj.publicize:
            raise Http404("Страница не найдена")

        return obj


class AnnouncementKGListView(ListView):
    template_name = 'pages/announcement_kg.html'
    queryset = Announcement.objects.all()
    context_object_name = 'announcements'


class AnnouncementKGDetailView(DetailView):
    model = Announcement
    template_name = 'pages/announcement_detail_kg.html'
    context_object_name = 'announcement'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)

        # Проверяем значение поля publicize
        if not obj.publicize_kg:
            raise Http404("Страница не найдена")

        return obj

