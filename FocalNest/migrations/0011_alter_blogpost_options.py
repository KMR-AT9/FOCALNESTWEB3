# Generated by Django 4.2.5 on 2023-11-16 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FocalNest', '0010_alter_blogpost_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'verbose_name': 'Blog', 'verbose_name_plural': 'Blogs'},
        ),
    ]
