# Generated by Django 2.1.7 on 2019-05-12 02:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testcase_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testcase',
            old_name='project',
            new_name='module',
        ),
    ]
