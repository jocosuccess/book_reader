# Generated by Django 2.2.1 on 2019-05-05 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('mp3', models.FileField(upload_to='audio')),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('creator', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('recorded', models.IntegerField(blank=True, default=None, null=True)),
                ('duration', models.IntegerField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('link', models.CharField(help_text='for example: https://vimeo.com/47160217', max_length=255)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('creator', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('recorded', models.IntegerField(blank=True, default=None, null=True)),
                ('duration', models.IntegerField(blank=True, default=None, null=True)),
            ],
        ),
    ]
