# Generated by Django 4.1.3 on 2022-11-23 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_application_is_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
