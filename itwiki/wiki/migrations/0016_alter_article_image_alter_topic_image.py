# Generated by Django 5.0.2 on 2024-04-27 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0015_delete_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='automation_programmability.png', upload_to='itwiki/itwiki/staticfiles/wiki/images'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='image',
            field=models.ImageField(default='automation_programmability.png', upload_to='itwiki/itwiki/staticfiles/wiki/images'),
        ),
    ]