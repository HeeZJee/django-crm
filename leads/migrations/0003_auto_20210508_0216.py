# Generated by Django 3.1 on 2021-05-08 02:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_auto_20210508_0214'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_oraganisor',
            new_name='is_organisor',
        ),
    ]