# Generated by Django 2.2.10 on 2020-03-09 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20200307_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default=None, max_length=100, verbose_name='Название текста'),
        ),
    ]
