# Generated by Django 4.2.4 on 2023-08-17 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lpg_locale', models.CharField(max_length=20)),
                ('lpg_euro', models.CharField(max_length=20)),
                ('diesel_locale', models.CharField(max_length=20)),
                ('diesel_euro', models.CharField(max_length=20)),
            ],
        ),
    ]