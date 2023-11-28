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


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название новости')
    date = models.DateField(verbose_name='Дата публикации', default=timezone.now)
    text = models.TextField(verbose_name='Текст публикации', blank=True)
    image = models.ImageField(verbose_name='Изображение',
                              upload_to=upload_image, blank=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title


class Feedback(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    contact_number = models.CharField(max_length=50, verbose_name='Номер телефона')
    email = models.EmailField(max_length=50, verbose_name='Электронная почта')
    message = models.TextField(max_length=455, verbose_name='Сообщение')
    attachment = models.FileField(upload_to='feedback_attachments/', null=True, blank=True)
    date = models.DateField(verbose_name='Дата публикации', default=timezone.now)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.date}"


class Contact(models.Model):
    number = models.CharField(max_length=50, verbose_name='Номер контакта')
    date = models.DateField(verbose_name='Дата публикации', default=timezone.now)
    text = models.TextField(verbose_name='Текст публикации', blank=True)

    def __str__(self):
        return self.text


class Announcement(models.Model):
    title = models.CharField(max_length=255, verbose_name='Объявления на русском')
    title_kg = models.CharField(max_length=255, verbose_name='Объявления на кыргызском')
    date = models.DateField(verbose_name='Дата публикации', default=timezone.now)
    text = models.TextField(verbose_name='Текст публикации на русском', blank=True)
    text_kg = models.TextField(verbose_name='Текст публикации на кыргызском', blank=True)
    file = models.FileField(verbose_name='Файл на русском', upload_to='media/', blank=True)
    file_kg = models.FileField(verbose_name='Файл на кыргызском', upload_to='media/', blank=True)
    image = models.ImageField(verbose_name='Изображение',
                              upload_to=upload_image, blank=True)
    publicize = models.BooleanField(verbose_name='Опубликовать русскую версию', default=False)
    publicize_kg = models.BooleanField(verbose_name='Опубликовать кыргызскую версию',default=False)

    class Meta:
        verbose_name = 'Объявления'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return f'{self.title} {self.title_kg}'

