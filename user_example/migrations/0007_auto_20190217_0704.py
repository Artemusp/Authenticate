# Generated by Django 2.1.3 on 2019-02-17 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_example', '0006_post_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.DateField(blank=True, null=True),
        ),
    ]
