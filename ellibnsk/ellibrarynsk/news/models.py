from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=100)
    anons = models.CharField('Анонс', max_length=255)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')
    count = models.IntegerField('Количество')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name='Новость'
        verbose_name_plural = 'Новости'


class CartUser(models.Model):
    user = models.CharField('Пользователь',max_length=100)
    books = models.IntegerField('Книги')
