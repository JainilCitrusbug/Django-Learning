# Generated by Django 4.0.3 on 2022-03-16 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.CharField(max_length=10)),
                ('course', models.CharField(max_length=70)),
            ],
        ),
    ]
