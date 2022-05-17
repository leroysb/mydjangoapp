# Generated by Django 4.0.4 on 2022-05-17 11:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_alter_user_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('e3cd33d2-2a0e-4174-a064-d45911a1cf73'), primary_key=True, serialize=False),
        ),
    ]
