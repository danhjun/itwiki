# Generated by Django 5.0.2 on 2024-02-27 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0009_alter_subtopic_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtopic',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]