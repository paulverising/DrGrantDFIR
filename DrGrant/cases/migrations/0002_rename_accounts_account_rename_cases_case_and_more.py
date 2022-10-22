# Generated by Django 4.1.2 on 2022-10-22 19:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cases', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Accounts',
            new_name='Account',
        ),
        migrations.RenameModel(
            old_name='Cases',
            new_name='Case',
        ),
        migrations.RenameModel(
            old_name='Systems',
            new_name='System',
        ),
        migrations.RenameModel(
            old_name='Tasks',
            new_name='Task',
        ),
    ]
