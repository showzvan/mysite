# Generated by Django 2.1.5 on 2019-03-01 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='verifycode',
            options={'verbose_name': '验证码表', 'verbose_name_plural': '验证码表'},
        ),
    ]