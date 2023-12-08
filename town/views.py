from django.db.models import Q
from django.http import Http404
from .models import News, Contact, Announcement, OfficialDocuments, History, TownHallManagement, PassportOfTown, Vacancy
from .form import FeedbackForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    # Получите все новости и отсортируйте их по дате в обратном порядке
    news_list = News.objects.all().order_by('-date')

    # Передайте отсортированный список в контекст для использования в шаблоне
    context = {'news_list': news_list[:9]}  # Выберите первые 9 новостей

    return render(request, 'pages/index.html', context)


class NewsListView(ListView):
    model = News
    template_name = 'pages/news_list.html'
    context_object_name = 'news_list'
    ordering = ['-date']
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(self.object_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            news_list = paginator.page(page)
        except PageNotAnInteger:
            # Если 'page' не является целым числом, передайте первую страницу
            news_list = paginator.page(1)
        except EmptyPage:
            # Если 'page' находится за пределами допустимого диапазона (e.g. 9999), передайте последнюю страницу
            news_list = paginator.page(paginator.num_pages)

        context['news_list'] = news_list
        return context


class NewsDetailView(DetailView):
    model = News
    template_name = 'pages/news_detail.html'
    context_object_name = 'news'


def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():

            feedback_instance = form.save()

            # Отправка уведомления на почту
            subject = 'Новый отзыв'
            message = render_to_string('email_templates/new_feedback_email.txt',
                                       {'feedback_instance': feedback_instance})
            from_email = 'esentur32@gmail.com'  # Замените на свою почту
            recipient_list = ['esentur32@gmail.com']  # Замените на свою почту

            email = EmailMessage(subject, message, from_email, recipient_list)

            # Если есть прикрепленные файлы
            for file in request.FILES.getlist('attachment'):
                email.attach(file.name, file.read(), file.content_type)

            email.send()

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_language = self.request.LANGUAGE_CODE

        # Если нет названия в соответствующем, тогда запись не будет возвращена на страницу.
        for announcement in context['announcements']:
            if current_language == 'ky' and not announcement.title_ky:
                announcement.title = 'Untitled'
            elif current_language == 'ru' and not announcement.title_ru:
                announcement.title = 'Untitled'

        return context


class AnnouncementDetailView(DetailView):
    model = Announcement
    template_name = 'pages/announcement_detail.html'
    context_object_name = 'announcement'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        current_language = self.request.LANGUAGE_CODE

        # Проверяем заголовок в соответствующем языке
        if current_language == 'ky' and not obj.title_ky:
            raise Http404("Страница не найдена")

        if current_language == 'ru' and not obj.title_ru:
            raise Http404("Страница не найдена")

        return obj


class OfficialDocumentsListView(ListView):
    template_name = 'pages/document.html'
    queryset = OfficialDocuments.objects.all()
    context_object_name = 'official_documents'
    ordering = ['-date']


class OfficialDocumentsDetailView(DetailView):
    model = OfficialDocuments
    template_name = 'pages/document_detail.html'
    context_object_name = 'official_document'

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


def passport_of_town(request):
    passport = PassportOfTown.objects.get(id=1)
    return render(request, 'pages/passport.html', {'passport': passport})


def vacancy(request):
    vacanc = Vacancy.objects.get(id=1)
    return render(request, 'pages/vacancy.html', {'vacancy': vacanc})
