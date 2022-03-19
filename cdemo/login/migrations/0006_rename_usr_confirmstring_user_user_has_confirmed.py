# Generated by Django 4.0.3 on 2022-03-19 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_confirmstring'),
    ]

    operations = [
        migrations.RenameField(
            model_name='confirmstring',
            old_name='usr',
            new_name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='has_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
