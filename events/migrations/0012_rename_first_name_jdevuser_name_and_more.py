# Generated by Django 4.1.1 on 2022-09-16 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_rename_name_jdevuser_first_name_jdevuser_last_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jdevuser',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='jdevuser',
            name='last_name',
        ),
    ]
