# Generated by Django 5.1.1 on 2024-09-25 15:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp_for_cinema', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seance',
            name='hall_connection',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='myapp_for_cinema.hall'),
            preserve_default=False,
        ),
    ]
