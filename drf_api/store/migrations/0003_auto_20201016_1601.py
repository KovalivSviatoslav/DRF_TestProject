# Generated by Django 3.1.2 on 2020-10-16 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(default='author', max_length=255),
            preserve_default=False,
        ),
    ]