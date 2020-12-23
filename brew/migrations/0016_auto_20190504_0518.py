# Generated by Django 3.0.dev20190414141414 on 2019-05-04 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brew', '0015_auto_20190502_2329'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acidity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acidity', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='brew',
            name='acidity',
        ),
        migrations.AlterField(
            model_name='brew',
            name='flavor',
            field=models.CharField(blank=True, choices=[(None, 'Taste like Coffee'), ('1', 'Fruity'), ('2', 'Sweet'), ('3', 'Nutty'), ('4', 'Woody'), ('5', 'Malty')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='brew',
            name='roastery',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='roast',
            name='notes',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='brew',
            name='acidity',
            field=models.ManyToManyField(to='brew.Acidity'),
        ),
    ]