# Generated by Django 5.0 on 2023-12-21 19:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdressUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adressuser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
