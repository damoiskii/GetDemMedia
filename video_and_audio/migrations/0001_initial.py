# Generated by Django 3.2.4 on 2021-06-20 04:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(blank=True, max_length=500, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('thumbnail', models.URLField(blank=True, null=True)),
                ('author', models.CharField(blank=True, max_length=500, null=True)),
                ('publish_date', models.DateField(auto_now=True)),
                ('views', models.CharField(blank=True, max_length=100, null=True)),
                ('length', models.CharField(blank=True, max_length=100, null=True)),
                ('api', models.CharField(blank=True, max_length=50, null=True)),
                ('mp3', models.FileField(blank=True, null=True, upload_to='audios/')),
                ('downloaded_on', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['name', '-downloaded_on'],
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(blank=True, max_length=500, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('thumbnail', models.URLField(blank=True, null=True)),
                ('author', models.CharField(blank=True, max_length=500, null=True)),
                ('publish_date', models.DateField(auto_now=True)),
                ('views', models.CharField(blank=True, max_length=100, null=True)),
                ('length', models.CharField(blank=True, max_length=100, null=True)),
                ('api', models.CharField(blank=True, max_length=50, null=True)),
                ('mp4', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('downloaded_on', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['name', '-downloaded_on'],
            },
        ),
    ]
