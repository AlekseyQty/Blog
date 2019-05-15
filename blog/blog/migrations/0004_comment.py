# Generated by Django 2.2 on 2019-05-09 17:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_is_hidden'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('creation_date', models.DateTimeField(default=datetime.datetime.now)),
                ('reply_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Comment')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.Post')),
            ],
        ),
    ]
