# Generated by Django 4.0 on 2022-03-10 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelname', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('gib', models.ImageField(default='default.png', upload_to='images')),
                ('price', models.CharField(max_length=255)),
                ('types', models.CharField(max_length=255)),
                ('format', models.CharField(max_length=255)),
                ('modeltype', models.CharField(max_length=255)),
                ('categori', models.CharField(max_length=255)),
                ('fbx', models.ImageField(default='default.png', upload_to='images')),
            ],
        ),
    ]
