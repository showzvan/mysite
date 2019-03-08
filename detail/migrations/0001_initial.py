# Generated by Django 2.1.5 on 2019-01-30 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_title', models.CharField(max_length=255, verbose_name='友情链接名称')),
                ('url', models.URLField(verbose_name='友情链接地址')),
                ('is_status', models.BooleanField(default=True, verbose_name='状态')),
            ],
            options={
                'verbose_name': '友情链接',
                'verbose_name_plural': '友情链接',
                'db_table': 'zhouju_links',
            },
        ),
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cityname', models.CharField(max_length=255, verbose_name='城市名称')),
                ('initials', models.CharField(default='A', max_length=10, verbose_name='首字母')),
                ('is_hot', models.BooleanField(default=False, verbose_name='是否热门')),
                ('is_status', models.BooleanField(default=True, verbose_name='是否可用')),
            ],
            options={
                'verbose_name': '首页地区表',
                'verbose_name_plural': '首页地区表',
                'db_table': 'zhouju_regions',
            },
        ),
    ]
