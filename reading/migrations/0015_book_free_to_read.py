# Generated by Django 2.2.1 on 2019-05-14 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reading', '0014_auto_20190510_0836'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='free_to_read',
            field=models.BooleanField(default=True),
        ),
    ]
