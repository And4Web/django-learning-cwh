# Generated by Django 4.0.6 on 2022-07-27 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='description',
            new_name='desc',
        ),
        migrations.AddField(
            model_name='contact',
            name='created_at',
            field=models.DateTimeField(default=1000),
        ),
    ]