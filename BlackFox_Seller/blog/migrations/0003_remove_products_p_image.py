# Generated by Django 4.0.3 on 2022-03-23 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='p_image',
        ),
    ]
