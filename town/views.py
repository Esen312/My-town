from django.db.models import Q
from django.http import Http404
from .models import (News, Contact, Announcement, OfficialDocuments, History, TownHallManagement, PassportOfTown,
                     Vacancy, Mayor)
from .form import FeedbackForm, NewsFilterForm, AnnouncementFilterForm, OfficialDocumentsFilterForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView, TemplateView
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class FilteredListView(ListView):
    template_name = None
    filter_form_class = None
    model = None
    context_object_name = None
    ordering = ['-date']
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        form = self.filter_form_class(self.request.GET)

        if form.is_valid():
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')

            if start_date:
                queryset = queryset.filter(date__gte=start_date)
            if end_date:
                queryset = queryset.filter(date__lte=end_date)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_language = self.request.LANGUAGE_CODE
        context['filter_form'] = self.filter_form_class(self.request.GET)

        # Фильтрация объектов по языку
        filtered_objects = [obj for obj in self.object_list if getattr(obj, f'title_{current_language}', None)]

        paginator = Paginator(filtered_objects, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            paginated_objects = paginator.page(page)
        except PageNotAnInteger:
            paginated_objects = paginator.page(1)
        except EmptyPage:
            paginated_objects = paginator.page(paginator.num_pages)

        context[self.context_object_name] = paginated_objects

        for obj in context[self.context_object_name]:
            # Проверка наличия языковых версий заголовков и установка заголовка "Untitled", если требуемая версия отсутствует
            title_attr = f'title_{current_language}'
            if not hasattr(obj, title_attr) or getattr(obj, title_attr) is None:
                obj.title = 'Untitled'

        return context


class LanguageCheckMixin:
    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        current_language = self.request.LANGUAGE_CODE

        # Проверяем заголовок в соответствующем языке
        if current_language == 'ky' and not getattr(obj, 'title_ky', None):
            raise Http404("Страница не найдена")

        if current_language == 'ru' and not getattr(obj, 'title_ru', None):
            raise Http404("Страница не найдена")

        return obj


def index(request):
    news_list = News.objects.all().order_by('-date')[:9]  # Выбираем первые 9 новостей
    mayor = Mayor.objects.first()
    context = {'news_list': news_list, 'mayor': mayor}

    current_language = request.LANGUAGE_CODE

    # Если нет названия в соответствующем языке, установите заголовок на "Untitled"
    for news in news_list:
        if current_language == 'ky' and not news.title_ky:
            news.title = 'Untitled'
        elif current_language == 'ru' and not news.title_ru:
            news.title = 'Untitled'

    return render(request, 'pages/index.html', context)


class NewsListView(FilteredListView):
    template_name = 'pages/news_list.html'
    filter_form_class = NewsFilterForm
    model = News
    context_object_name = 'news_list'


class NewsDetailView(LanguageCheckMixin, DetailView):
    model = News
    template_name = 'pages/news_detail.html'
    context_object_name = 'news'


class AnnouncementListView(FilteredListView):
    template_name = 'pages/announcement.html'
    filter_form_class = AnnouncementFilterForm
    model = Announcement
    context_object_name = 'announcements'


class AnnouncementDetailView(LanguageCheckMixin, DetailView):
    model = Announcement
    template_name = 'pages/announcement_detail.html'
    context_object_name = 'announcement'


class OfficialDocumentsListView(FilteredListView):
    template_name = 'pages/document.html'
    filter_form_class = OfficialDocumentsFilterForm
    model = OfficialDocuments
    context_object_name = 'official_documents'


class OfficialDocumentsDetailView(LanguageCheckMixin, DetailView):
    model = OfficialDocuments
    template_name = 'pages/document_detail.html'
    context_object_name = 'official_document'


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
        announcements = Announcement.objects.filter(Q(title__icontains=query))
        documents = OfficialDocuments.objects.filter(Q(title__icontains=query))
        news = News.objects.filter(Q(title__icontains=query))

        results = []
        for announcement in announcements:
            results.append({'model_name': 'announcement', 'object': announcement})
        for document in documents:
            results.append({'model_name': 'document', 'object': document})
        for item in news:
            results.append({'model_name': 'news', 'object': item})

        paginator = Paginator(results, 2)  # 10 объектов на странице
        page = request.GET.get('page')

        try:
            results = paginator.page(page)
        except PageNotAnInteger:
            # Если 'page' не является целым числом, передайте первую страницу
            results = paginator.page(1)
        except EmptyPage:
            # Если 'page' находится за пределами допустимого диапазона, передайте последнюю страницу
            results = paginator.page(paginator.num_pages)

        context = {
            'results': results,
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


class MapView(TemplateView):
    template_name = 'pages/map.html'


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
