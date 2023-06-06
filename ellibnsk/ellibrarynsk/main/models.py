from django.db import models

class News(models.Model):
    title = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

class Banner(models.Model):
    title = models.CharField('Название', max_length=100)
    date = models.DateTimeField('Дата')
    url = models.CharField('Источник', max_length = 100)
    img = models.CharField('Изображение', max_length = 100)
    def __str__(self):
        return self.title