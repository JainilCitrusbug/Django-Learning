# Generated by Django 3.1.4 on 2020-12-09 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customadmin', '0005_shopproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopproduct',
            name='detail',
            field=models.TextField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='shopproduct',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
