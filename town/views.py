from django.conf import settings
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView
from .models import News, Contact
from .form import FeedbackForm
from django.shortcuts import render, redirect
from django.contrib import messages


def index(request):
    new_list = News.objects.all()
    return render(request, 'pages/index.html', {'news_list': new_list})


class NewsListView(ListView):
    model = News
    template_name = 'pages/news_list.html'
    context_object_name = 'news_list'
    ordering = ['-date']


class NewsDetailView(DetailView):
    model = News
    template_name = 'pages/news_detail.html'
    context_object_name = 'news'


from django.core.mail import send_mail
from django.template.loader import render_to_string

from django.core.mail import EmailMessage
from django.template.loader import render_to_string


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