# Generated by Django 4.2.7 on 2023-12-09 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proffessional', '0004_project'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='challenges',
            new_name='features',
        ),
    ]
