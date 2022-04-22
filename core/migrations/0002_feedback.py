# Generated by Django 4.0.4 on 2022-04-22 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('postdate', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(max_length=500)),
                ('ratings', models.IntegerField()),
                ('source', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'feedback',
                'ordering': ['-postdate'],
            },
        ),
    ]
