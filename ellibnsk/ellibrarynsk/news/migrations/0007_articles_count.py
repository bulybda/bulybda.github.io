# Generated by Django 4.2.1 on 2023-05-31 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_alter_cartuser_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='count',
            field=models.IntegerField(default=1, verbose_name='Количество'),
            preserve_default=False,
        ),
    ]
