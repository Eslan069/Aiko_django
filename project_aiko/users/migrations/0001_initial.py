# Generated by Django 5.1.4 on 2025-01-22 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12)),
                ('lastName', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]
