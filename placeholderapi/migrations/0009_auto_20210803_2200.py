# Generated by Django 3.1.7 on 2021-08-03 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placeholderapi', '0008_todo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
    ]
