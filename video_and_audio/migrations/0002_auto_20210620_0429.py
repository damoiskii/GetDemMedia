# Generated by Django 3.2.4 on 2021-06-20 09:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('video_and_audio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='publish_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='video',
            name='publish_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
