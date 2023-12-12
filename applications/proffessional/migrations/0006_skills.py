# Generated by Django 4.2.7 on 2023-12-11 15:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proffessional', '0005_rename_challenges_project_features'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('skiill', models.CharField(blank=True, max_length=50, null=True)),
                ('rating', models.CharField(blank=True, max_length=10, null=True)),
                ('years_of_experience', models.CharField(blank=True, max_length=5, null=True)),
                ('organization', models.CharField(blank=True, max_length=155, null=True)),
                ('version', models.CharField(blank=True, max_length=10, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]