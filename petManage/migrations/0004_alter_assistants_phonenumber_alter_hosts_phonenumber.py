# Generated by Django 4.0.4 on 2022-06-01 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petManage', '0003_alter_assistants_phonenumber_alter_hosts_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assistants',
            name='phonenumber',
            field=models.CharField(max_length=10, verbose_name='聯絡號碼'),
        ),
        migrations.AlterField(
            model_name='hosts',
            name='phonenumber',
            field=models.CharField(max_length=10, verbose_name='聯絡號碼'),
        ),
    ]
