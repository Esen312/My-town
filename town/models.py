from django.db import models
from django.utils import timezone

from town.upload_image import upload_image


class Announcement(models.Model):
    title = models.CharField(max_length=255, verbose_name='Объявления')
    date = models.DateField(verbose_name='Дата публикации', default=timezone.now)
    text = models.TextField(verbose_name='Текст публикации', blank=True)
    file = models.FileField(verbose_name='Файл', upload_to='media/', blank=True)
    image = models.ImageField(verbose_name='Изображение',
                              upload_to=upload_image, blank=True)

    class Meta:
        verbose_name = 'Объявления'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.title
