# Generated by Django 3.2.13 on 2022-07-01 08:45

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0002_auto_20220630_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='accident',
            name='the_json',
            field=jsonfield.fields.JSONField(default=dict),
        ),
    ]
