# Generated by Django 2.2 on 2019-04-24 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190421_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_hidden',
            field=models.BooleanField(default=False),
        ),
    ]
