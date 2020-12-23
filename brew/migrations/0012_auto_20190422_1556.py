# Generated by Django 3.0.dev20190414141414 on 2019-04-22 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brew', '0011_auto_20190422_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brew',
            name='flavor',
            field=models.IntegerField(blank=True, choices=[(1, 'Fruity'), (2, 'Sweet'), (3, 'Nutty'), (4, 'Woody'), (5, 'Malty')], default=1, null=True),
        ),
    ]