# Generated by Django 4.0.3 on 2022-03-22 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0007_product_product_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_author',
        ),
    ]
