from django.db import models
from django.utils import timezone
from town.upload_image import upload_image


class Announcement(models.Model):
    title = models.CharField(max_length=255, verbose_name='Объявления[ru]')
    title_kg = models.CharField(max_length=255, verbose_name='Объявления[kg]', blank=True)
    date = models.DateField(verbose_name='Дата публикации', default=timezone.now)
    text = models.TextField(verbose_name='Текст публикации[ru]', blank=True)
    text_kg = models.TextField(verbose_name='Текст публикации[kg]', blank=True)
    file = models.FileField(verbose_name='Файл[ru]', upload_to='media/', blank=True)
    file_kg = models.FileField(verbose_name='Файл[kg]', upload_to='media/', blank=True)
    publicize = models.BooleanField(verbose_name='Опубликовать русскую версию', default=False)
    publicize_kg = models.BooleanField(verbose_name='Опубликовать кыргызскую версию', default=False)

    def get_photos(self):
        return Photo.objects.filter(publication=self)

    class Meta:
        verbose_name = 'Объявления'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return f'{self.title} {self.title_kg}'


class Photo(models.Model):
    publication = models.ForeignKey(Announcement, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_image)


class OfficialDocuments(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название[ru]')
    title_kg = models.CharField(max_length=255, verbose_name='Название[kg]', blank=True)
    date = models.DateField(verbose_name='Дата публикации', default=timezone.now)
    text = models.TextField(verbose_name='Текст[ru]', blank=True)
    text_kg = models.TextField(verbose_name='Текст[kg]', blank=True)
    file = models.FileField(verbose_name='Файл[ru]', upload_to='media/', blank=True)
    file_kg = models.FileField(verbose_name='Файл[kg]', upload_to='media/', blank=True)
    image = models.ImageField(verbose_name='Изображение',
                              upload_to=upload_image, blank=True)
    publicize = models.BooleanField(verbose_name='Опубликовать русскую версию', default=False)
    publicize_kg = models.BooleanField(verbose_name='Опубликовать кыргызскую версию', default=False)

    class Meta:
        verbose_name = 'Социальное и экономическое развитие'
        verbose_name_plural = 'Социальное и экономическое развитие'

    def __str__(self):
        return f'{self.title} {self.title_kg}'


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
    text_kg = models.TextField(verbose_name='Текст[kg]', blank=True)
    image = models.ImageField(verbose_name='Изображение', upload_to=upload_image, blank=True)

    class Meta:
        verbose_name = 'История'
        verbose_name_plural = 'История'

    def __str__(self):
        return self.title


class TownHallManagement(models.Model):
    first_name = models.CharField(verbose_name='Имя[ru]', max_length=50)
    first_name_kg = models.CharField(verbose_name='Имя[kg]', max_length=50)
    last_name = models.CharField(verbose_name='Фамилия[ru]', max_length=50)
    last_name_kg = models.CharField(verbose_name='Фамилия[kg]', max_length=50)
    middle_name = models.CharField(verbose_name='Отчество[ru]', max_length=50)
    middle_name_kg = models.CharField(verbose_name='Отчество[kg]', max_length=50)
    position = models.CharField(verbose_name='Должность[ru]', max_length=120)
    position_kg = models.CharField(verbose_name='Должность[kg]', max_length=120)
    image = models.ImageField(verbose_name='Изображение', upload_to=upload_image)
    birth_date = models.DateField(verbose_name='Дата рождения', default=timezone.now)
    education = models.TextField(verbose_name='Образование[ru]')
    education_kg = models.TextField(verbose_name='Образование[kg]')
    work_experience = models.TextField(verbose_name='Опыт работы[ru]')
    work_experience_kg = models.TextField(verbose_name='Опыт работы[kg]')

    class Meta:
        verbose_name = 'Руководитель мэрии'
        verbose_name_plural = 'Руководители мэрии'

    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'
