# Generated by Django 2.2.5 on 2019-12-28 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webSite', '0016_auto_20191228_0402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='grade_type',
            field=models.CharField(choices=[('by student', 'by student'), ('by professor', 'by professor'), ('by industry', 'by industry')], max_length=256),
        ),
    ]