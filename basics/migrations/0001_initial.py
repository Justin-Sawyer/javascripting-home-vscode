# Generated by Django 3.2.7 on 2021-11-08 12:38

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('summary', models.CharField(max_length=500)),
                ('description', tinymce.models.HTMLField()),
                ('script_title_1', models.CharField(blank=True, default=None, max_length=254, null=True)),
                ('script_1', models.URLField(blank=True, default=None, max_length=2000, null=True)),
                ('gist_title_1', models.CharField(blank=True, max_length=254, null=True)),
                ('gist_1', models.CharField(blank=True, max_length=2000, null=True)),
                ('codepen_title_1', models.CharField(blank=True, max_length=254, null=True)),
                ('codepen_data_slug_hash_1', models.CharField(blank=True, max_length=254, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('category', models.ManyToManyField(to='basics.Category')),
            ],
        ),
    ]
