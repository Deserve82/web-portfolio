# Generated by Django 3.1.1 on 2020-09-18 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200918_1728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='git_hub_link',
        ),
    ]