# Generated by Django 2.2.5 on 2019-12-19 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webSite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='PresentationStudent',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='file', to='webSite.PresentationStudent'),
        ),
        migrations.AddField(
            model_name='presentationstudent',
            name='guid_instructor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='webSite.Professor'),
        ),
        migrations.AddField(
            model_name='presentationstudent',
            name='research_subject',
            field=models.CharField(default=None, max_length=256),
            preserve_default=False,
        ),
    ]
