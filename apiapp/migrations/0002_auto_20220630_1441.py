# Generated by Django 3.2.13 on 2022-06-30 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accident',
            name='month',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='accident',
            name='year',
            field=models.CharField(max_length=6),
        ),
    ]