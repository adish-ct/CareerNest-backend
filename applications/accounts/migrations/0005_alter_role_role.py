# Generated by Django 4.2.7 on 2023-11-16 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_role_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='role',
            field=models.CharField(blank=True, default='CANDIDATE', null=True, unique=True),
        ),
    ]
