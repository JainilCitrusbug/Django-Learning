# Generated by Django 4.0.3 on 2022-03-24 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
