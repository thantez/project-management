# Generated by Django 2.2.5 on 2019-12-28 00:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webSite', '0015_auto_20191228_0216'),
    ]

    operations = [
        migrations.RenameField(
            model_name='semester',
            old_name='is_active',
            new_name='active',
        ),
    ]