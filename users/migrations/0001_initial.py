# Generated by Django 3.2.6 on 2024-05-03 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('login', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('isConfirmed', models.BooleanField(default=False)),
            ],
        ),
    ]
