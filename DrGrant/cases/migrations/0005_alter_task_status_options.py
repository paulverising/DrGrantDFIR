# Generated by Django 4.1.2 on 2022-10-23 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0004_alter_task_status_options_alter_task_assignee'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task_status',
            options={'verbose_name_plural': 'Task_statuses'},
        ),
    ]