# Generated by Django 5.1 on 2024-08-18 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0004_remove_item_location_delete_location'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
