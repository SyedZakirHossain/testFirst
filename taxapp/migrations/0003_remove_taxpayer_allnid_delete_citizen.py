# Generated by Django 4.1.5 on 2023-01-20 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxapp', '0002_taxpayer_rename_allnid_citizen_delete_taxlisted_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taxpayer',
            name='allnid',
        ),
        migrations.DeleteModel(
            name='Citizen',
        ),
    ]
