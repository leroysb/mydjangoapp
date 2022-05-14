# Generated by Django 4.0.4 on 2022-05-14 19:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_user_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('a58b593d-e5be-4472-9cba-ffd4a8736da5'), primary_key=True, serialize=False),
        ),
    ]
