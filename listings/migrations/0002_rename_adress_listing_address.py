# Generated by Django 4.0.4 on 2022-06-01 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='adress',
            new_name='address',
        ),
    ]
