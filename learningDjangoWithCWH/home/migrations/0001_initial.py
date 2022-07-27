# Generated by Django 4.0.6 on 2022-07-27 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
    ]