# Generated by Django 3.2.7 on 2021-11-08 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_date_creationdate'),
        ('basics', '0004_remove_article_new_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='new_date_added',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='added_date', to='home.creationdate'),
        ),
    ]