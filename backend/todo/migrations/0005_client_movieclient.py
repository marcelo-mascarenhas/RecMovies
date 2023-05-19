# Generated by Django 4.2.1 on 2023-05-19 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_alter_movies_release_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('instrument_purchase', models.CharField(max_length=100)),
                ('address_line1', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MovieClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.client')),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.movies')),
            ],
        ),
    ]