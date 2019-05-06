# Generated by Django 3.0.dev20190414141414 on 2019-05-04 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brew', '0018_auto_20190504_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roast',
            name='batch_size',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='roast',
            name='first_crack_end',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='roast',
            name='first_crack_start',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='roast',
            name='roast_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='roast',
            name='roast_time',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='roast',
            name='second_crack_start',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
