# Generated by Django 2.2 on 2019-09-07 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0012_auto_20190907_1741'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Applicants',
            new_name='Applicant',
        ),
        migrations.RenameModel(
            old_name='Jobs',
            new_name='Job',
        ),
        migrations.RenameModel(
            old_name='questions',
            new_name='question',
        ),
    ]