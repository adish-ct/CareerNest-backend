# Generated by Django 4.2.7 on 2023-12-04 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_profile_additional_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='phone',
            new_name='mobile',
        ),
    ]