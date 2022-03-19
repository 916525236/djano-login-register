# Generated by Django 4.0.3 on 2022-03-16 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_user_m_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfirmString',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=256)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
                ('usr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='login.user')),
            ],
            options={
                'verbose_name': '确认码',
                'verbose_name_plural': '确认码',
                'ordering': ['-c_time'],
            },
        ),
    ]
