# Generated by Django 5.0.2 on 2024-02-18 21:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wiki.article'),
        ),
    ]
