# Generated by Django 4.2.1 on 2023-05-19 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_alter_movies_available_copies'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='money',
            field=models.FloatField(default=0.0),
        ),
    ]