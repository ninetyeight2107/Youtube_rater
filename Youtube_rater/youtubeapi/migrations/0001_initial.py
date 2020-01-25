# Generated by Django 2.2.7 on 2019-11-29 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('description', models.TextField(max_length=500)),
                ('url', models.URLField(max_length=300)),
                ('category', models.CharField(max_length=16)),
                ('subcategory', models.TextField(max_length=50)),
                ('autho', models.TextField(max_length=50)),
            ],
        ),
    ]
