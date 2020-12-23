# Generated by Django 3.0.dev20190414141414 on 2019-04-18 07:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brew', '0006_auto_20190418_0750'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coffee_name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('roast_levels', models.IntegerField(choices=[(1, 'Light'), (2, 'Medium'), (3, 'Dark')], null=True)),
                ('methods', models.IntegerField(choices=[(1, 'Pour_Over'), (2, 'AiroPress'), (3, 'French_Press')], null=True)),
                ('rates', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5)])),
            ],
        ),
    ]