# Generated by Django 3.2.3 on 2021-06-13 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Daily',
            new_name='Recipe',
        ),
    ]
