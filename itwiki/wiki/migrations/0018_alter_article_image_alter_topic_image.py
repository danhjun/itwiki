# Generated by Django 5.0.2 on 2024-04-28 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0017_alter_article_image_alter_topic_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='automation_programmability.png', upload_to='wiki/images'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='image',
            field=models.ImageField(default='automation_programmability.png', upload_to='wiki/images'),
        ),
    ]
