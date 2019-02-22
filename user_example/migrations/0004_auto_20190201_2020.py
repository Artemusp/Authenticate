# Generated by Django 2.1.3 on 2019-02-01 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_example', '0003_post_video_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='rating',
            field=models.CharField(default=0, max_length=2),
        ),
        migrations.AlterField(
            model_name='post',
            name='video_url',
            field=models.CharField(default='link', max_length=200),
        ),
    ]