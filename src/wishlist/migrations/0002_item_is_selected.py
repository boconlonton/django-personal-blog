# Generated by Django 3.2 on 2021-04-12 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_selected',
            field=models.BooleanField(default=False),
        ),
    ]
