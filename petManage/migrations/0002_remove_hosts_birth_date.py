# Generated by Django 4.0.4 on 2022-06-02 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petManage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hosts',
            name='birth_date',
        ),
    ]
