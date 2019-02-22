# Generated by Django 2.1.3 on 2019-02-18 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_example', '0010_auto_20190218_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='height',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, height_field='height', null=True, upload_to='', width_field='width'),
        ),
        migrations.AddField(
            model_name='profile',
            name='width',
            field=models.IntegerField(default=0),
        ),
    ]
