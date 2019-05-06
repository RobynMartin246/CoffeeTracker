# Generated by Django 3.0.dev20190414141414 on 2019-04-21 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brew', '0009_auto_20190421_0855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brew',
            name='rates',
        ),
        migrations.AddField(
            model_name='brew',
            name='acidity',
            field=models.IntegerField(blank=True, choices=[(1, 'Mellow'), (2, 'Winey'), (3, 'Citrus'), (4, 'Sour'), (5, 'Berry-like')], default=1, null=True),
        ),
        migrations.AddField(
            model_name='brew',
            name='flavor',
            field=models.IntegerField(blank=True, choices=[(1, 'Fruity'), (2, 'Sweet'), (3, 'Nutty'), (4, 'Woody')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='brew',
            name='methods',
            field=models.IntegerField(choices=[(1, 'Pour_Over'), (2, 'AiroPress'), (3, 'French_Press'), (4, 'Drip'), (5, 'Unknown')], default=1),
        ),
        migrations.AlterField(
            model_name='brew',
            name='roast_levels',
            field=models.IntegerField(choices=[(1, 'Light'), (2, 'Medium'), (3, 'Dark'), (4, 'Unknown')], default=1),
        ),
    ]
