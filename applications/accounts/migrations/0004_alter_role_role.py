# Generated by Django 4.2.7 on 2023-11-16 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_is_approved_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='role',
            field=models.CharField(blank=True, default='CANDIDATE', null=True),
        ),
    ]
