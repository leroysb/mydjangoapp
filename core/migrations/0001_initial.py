# Generated by Django 3.2.9 on 2021-11-22 11:08

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='core/podcast/')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('appleurl', models.URLField(max_length=255, unique=True)),
                ('googleurl', models.URLField(max_length=255, unique=True)),
                ('spotifyurl', models.URLField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'podcast',
            },
        ),
        migrations.CreateModel(
            name='Privacy',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('content', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Terms',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('content', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='PodcastEpisode',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('season', models.IntegerField()),
                ('episode', models.IntegerField()),
                ('title', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='core/podcast/')),
                ('summary', models.CharField(max_length=500)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('audio', models.FileField(upload_to='core/podcast/')),
                ('pubDate', models.DateField()),
                ('podcast', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episodes', to='core.podcast')),
            ],
            options={
                'db_table': 'podcast_episode',
                'ordering': ['-episode'],
            },
        ),
    ]
