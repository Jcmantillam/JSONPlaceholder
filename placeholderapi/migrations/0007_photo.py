# Generated by Django 3.1.7 on 2021-08-03 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('placeholderapi', '0006_album'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=300)),
                ('thumbnailUrl', models.CharField(max_length=300)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='placeholderapi.album')),
            ],
        ),
    ]