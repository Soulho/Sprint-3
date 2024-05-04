# Generated by Django 3.2.6 on 2024-05-04 01:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_auto_20240503_2005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authentications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(blank=True, default=None, null=True)),
                ('dateTime', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]