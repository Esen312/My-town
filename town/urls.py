from .views import NewsListView, NewsDetailView, feedback, contact_view
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('news/', NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('feedback/', feedback, name='feedback'),
    path('contact/', contact_view, name='contact'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)