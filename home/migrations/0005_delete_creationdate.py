# Generated by Django 3.2.7 on 2021-11-08 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_date_created_creationdate_this_date_created'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CreationDate',
        ),
    ]
