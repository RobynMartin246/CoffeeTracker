# Generated by Django 3.0.dev20190414141414 on 2019-04-22 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brew', '0010_auto_20190421_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brew',
            name='flavor',
            field=models.IntegerField(blank=True, choices=[(1, 'Mellow'), (2, 'Winey'), (3, 'Citrus'), (4, 'Sour'), (5, 'Berry-like')], default=1, null=True),
        ),
    ]
