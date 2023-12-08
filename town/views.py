from django.db.models import Q
from django.http import Http404
from .models import News, Contact, Announcement, OfficialDocuments, History, TownHallManagement, PassportOfTown, Mayor
from .form import FeedbackForm, NewsFilterForm, AnnouncementFilterForm, OfficialDocumentsFilterForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView, TemplateView
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    news_list = News.objects.all().order_by('-date')
    mayor = Mayor.objects.first()
    context = {'news_list': news_list[:9], 'mayor': mayor}  # Выберите первые 9 новостей
    return render(request, 'pages/index.html', context)


class NewsListView(ListView):
    model = News
    template_name = 'pages/news_list.html'
    context_object_name = 'news_list'
    ordering = ['-date']
    paginate_by = 2

    def get_custom_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(self.object_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            news_list = paginator.page(page)
        except PageNotAnInteger:
            # Если 'page' не является целым числом, передайте первую страницу
            news_list = paginator.page(1)
        except EmptyPage:
            # Если 'page' находится за пределами допустимого диапазона (например, 9999), передайте последнюю страницу
            news_list = paginator.page(paginator.num_pages)

        context['news_list'] = news_list
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = NewsFilterForm(self.request.GET)

        if form.is_valid():
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')

            if start_date:
                queryset = queryset.filter(date__gte=start_date)
            if end_date:
                queryset = queryset.filter(date__lte=end_date)

        return queryset

    def get_context_data(self, **kwargs):
        context = self.get_custom_context_data(**kwargs)
        context['filter_form'] = NewsFilterForm(self.request.GET)
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
    model = Announcement
    context_object_name = 'announcements'
    ordering = ['-date']
    paginate_by = 2  # Количество объявлений на одной странице

    def get_queryset(self):
        return Announcement.objects.filter(publicize=True)

    def get_custom_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(self.object_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            announcements = paginator.page(page)
        except PageNotAnInteger:
            # Если 'page' не является целым числом, передайте первую страницу
            announcements = paginator.page(1)
        except EmptyPage:
            # Если 'page' находится за пределами допустимого диапазона, передайте последнюю страницу
            announcements = paginator.page(paginator.num_pages)

        context['announcements'] = announcements
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = AnnouncementFilterForm(self.request.GET)

        if form.is_valid():
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')

            if start_date:
                queryset = queryset.filter(date__gte=start_date)
            if end_date:
                queryset = queryset.filter(date__lte=end_date)

        return queryset

    def get_context_data(self, **kwargs):
        context = self.get_custom_context_data(**kwargs)
        context['filter_form'] = AnnouncementFilterForm(self.request.GET)
        return context


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
    template_name = 'pages/document.html'
    queryset = OfficialDocuments.objects.all()
    context_object_name = 'official_documents'
    ordering = ['-date']
    paginate_by = 2  # Количество объявлений на одной странице

    def get_queryset(self):
        return OfficialDocuments.objects.filter(publicize=True)

    def get_custom_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(self.object_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            announcements = paginator.page(page)
        except PageNotAnInteger:
            # Если 'page' не является целым числом, передайте первую страницу
            announcements = paginator.page(1)
        except EmptyPage:
            # Если 'page' находится за пределами допустимого диапазона, передайте последнюю страницу
            announcements = paginator.page(paginator.num_pages)

        context['document'] = announcements
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = OfficialDocumentsFilterForm(self.request.GET)

        if form.is_valid():
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')

            if start_date:
                queryset = queryset.filter(date__gte=start_date)
            if end_date:
                queryset = queryset.filter(date__lte=end_date)

        return queryset

    def get_context_data(self, **kwargs):
        context = self.get_custom_context_data(**kwargs)
        context['filter_form'] = OfficialDocumentsFilterForm(self.request.GET)
        return context


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


class MapView(TemplateView):
    template_name = 'pages/map.html'