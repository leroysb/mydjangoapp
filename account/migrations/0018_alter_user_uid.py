# Generated by Django 4.0.4 on 2022-05-21 13:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_alter_user_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('29e0cb15-fefa-4760-869c-d6f23f4bb145'), primary_key=True, serialize=False),
        ),
    ]
