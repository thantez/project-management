# Generated by Django 2.2.5 on 2019-12-19 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webSite', '0003_auto_20191219_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='doc1',
            field=models.FileField(blank=True, upload_to='doc2'),
        ),
        migrations.DeleteModel(
            name='File',
        ),
    ]
