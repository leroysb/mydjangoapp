# Generated by Django 4.0.1 on 2022-01-20 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_feedback_sourceid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='source',
        ),
    ]
