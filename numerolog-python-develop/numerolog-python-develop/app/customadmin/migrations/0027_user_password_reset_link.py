# Generated by Django 3.1.4 on 2021-01-29 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customadmin', '0026_service_related_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password_reset_link',
            field=models.UUIDField(blank=True, null=True, unique=True),
        ),
    ]
