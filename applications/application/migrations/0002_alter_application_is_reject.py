# Generated by Django 4.2.7 on 2023-12-11 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='is_reject',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
