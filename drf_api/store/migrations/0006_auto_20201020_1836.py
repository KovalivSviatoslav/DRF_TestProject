# Generated by Django 3.1.2 on 2020-10-20 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20201020_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbookrelation',
            name='rate',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Ok'), (2, 'Fine'), (3, 'Cool'), (4, 'Amazing'), (5, 'Incredible')], null=True),
        ),
    ]
