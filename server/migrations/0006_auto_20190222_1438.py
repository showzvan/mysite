# Generated by Django 2.1.5 on 2019-02-22 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0005_auto_20190222_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aquestions',
            name='leval',
            field=models.CharField(choices=[(0, '高起专'), (1, '高起本'), (2, '专升本')], default='gqb', max_length=3, verbose_name='所属层次'),
        ),
    ]
