# Generated by Django 4.1.1 on 2022-09-16 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_alter_eventregisteration_id_alter_register_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='Organization',
            new_name='Branch',
        ),
    ]
