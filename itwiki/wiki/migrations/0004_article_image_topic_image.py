# Generated by Django 5.0.2 on 2024-02-24 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0003_article_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default='automation_programmability.png', upload_to='itwiki/wiki/static/wiki/images'),
        ),
        migrations.AddField(
            model_name='topic',
            name='image',
            field=models.ImageField(default='automation_programmability.png', upload_to='itwiki/wiki/static/wiki/images'),
        ),
    ]