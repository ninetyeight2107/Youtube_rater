# Generated by Django 2.2.7 on 2019-12-01 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youtubeapi', '0004_auto_20191130_0901'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='autho',
            new_name='author',
        ),
    ]
