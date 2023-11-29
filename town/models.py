from django.db import models
from django.utils import timezone
from town.upload_image import upload_image


class Announcement(models.Model):
    title = models.CharField(max_length=255, verbose_name='Объявления')
    date = models.DateField(verbose_name='Дата публикации', default=timezone.now)
    text = models.TextField(verbose_name='Текст публикации', blank=True, null=True)
    file = models.FileField(verbose_name='Файл[ru]', upload_to='media/', blank=True)
    file_kg = models.FileField(verbose_name='Файл[ky]', upload_to='media/', blank=True)
    publicize = models.BooleanField(verbose_name='Опубликовать русскую версию', default=False)

    def get_photos(self):
        return Photo.objects.filter(publication=self)

    class Meta:
        verbose_name = 'Объявления'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.title


class Photo(models.Model):
    publication = models.ForeignKey(Announcement, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_image)


class OfficialDocuments(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название[ru]')
    date = models.DateField(verbose_name='Дата публикации', default=timezone.now)
    text = models.TextField(verbose_name='Текст[ru]', blank=True)
    file = models.FileField(verbose_name='Файл[ru]', upload_to='media/', blank=True)
    image = models.ImageField(verbose_name='Изображение',
                              upload_to=upload_image, blank=True)
    publicize = models.BooleanField(verbose_name='Опубликовать русскую версию', default=False)

    class Meta:
        verbose_name = 'Социальное и экономическое развитие'
        verbose_name_plural = 'Социальное и экономическое развитие'

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


class History(models.Model):
    title = models.CharField(verbose_name='История', max_length=40)
    date = models.DateField(verbose_name='Дата публикации', default=timezone.now)
    text = models.TextField(verbose_name='Текст[ru]', blank=True)

    def get_photos(self):
        return HistoryPhoto.objects.filter(publication=self)

    class Meta:
        verbose_name = 'История'
        verbose_name_plural = 'История'

    def __str__(self):
        return self.title


class HistoryPhoto(models.Model):
    publication = models.ForeignKey(History, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_image)


class TownHallManagement(models.Model):
    first_name = models.CharField(verbose_name='Имя[ru]', max_length=50)
    last_name = models.CharField(verbose_name='Фамилия[ru]', max_length=50)
    middle_name = models.CharField(verbose_name='Отчество[ru]', max_length=50)
    position = models.CharField(verbose_name='Должность[ru]', max_length=120)
    image = models.ImageField(verbose_name='Изображение', upload_to=upload_image)
    birth_date = models.DateField(verbose_name='Дата рождения', default=timezone.now)
    education = models.TextField(verbose_name='Образование[ru]')
    work_experience = models.TextField(verbose_name='Опыт работы[ru]')

    class Meta:
        verbose_name = 'Руководитель мэрии'
        verbose_name_plural = 'Руководители мэрии'

    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'
