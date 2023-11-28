from django.views.generic import ListView, DetailView
from .models import News, Contact
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