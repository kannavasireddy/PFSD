# Generated by Django 4.1.1 on 2022-09-16 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_rename_organization_jdevuser_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jdevuser',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
