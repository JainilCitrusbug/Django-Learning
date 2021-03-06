# Generated by Django 3.1.4 on 2021-03-19 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customadmin', '0031_servicecategory_category_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date when created.', null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date when updated.', null=True, verbose_name='Updated At')),
                ('category_image', models.ImageField(blank=True, null=True, upload_to='categories')),
                ('service_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customadmin.servicecategory')),
            ],
            options={
                'verbose_name': 'CategoryImage',
                'verbose_name_plural': 'Category Images',
                'ordering': ['-created_at'],
            },
        ),
    ]
