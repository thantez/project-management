# Generated by Django 2.2.5 on 2019-12-27 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webSite', '0010_auto_20191227_0635'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='research_subject',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
