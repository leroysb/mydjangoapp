# Generated by Django 4.0.3 on 2022-03-28 12:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_user_is_deactivated_alter_user_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='alias',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9_]{4,10}$', message="Username should be between 4-10 characters, and must contain letters, numbers, or '_' only.")], verbose_name='Username'),
        ),
    ]
