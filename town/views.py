from django.views.generic import ListView, DetailView
from .models import News, Contact
from .form import FeedbackForm
from django.shortcuts import render, redirect
from django.contrib import messages
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