# Generated by Django 3.2.8 on 2021-11-26 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jinjatemp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('technology', models.CharField(max_length=20)),
                ('image', models.FilePathField(path='/img')),
            ],
        ),
    ]
