# Generated by Django 4.2.3 on 2023-07-03 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='tecnology',
            new_name='technology',
        ),
    ]