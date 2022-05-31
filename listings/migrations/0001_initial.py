# Generated by Django 4.0.4 on 2022-05-31 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('price', models.IntegerField()),
                ('bedroom', models.IntegerField()),
                ('bathroom', models.IntegerField()),
                ('square_feet', models.IntegerField()),
                ('adress', models.CharField(max_length=150)),
            ],
        ),
    ]
