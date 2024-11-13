# Generated by Django 5.1.1 on 2024-10-09 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp_for_cinema', '0004_remove_armchair_number_hall_hall_number_hall'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='price_info',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='title',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='type_ticket',
        ),
        migrations.AddField(
            model_name='film',
            name='price_info',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
