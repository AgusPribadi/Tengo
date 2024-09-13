# Generated by Django 4.2.3 on 2023-07-23 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "aplikasi_tengo",
            "0005_coffeeshop_video_url_alter_coffeeshop_alamat_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(model_name="coffeeshop", name="video_url",),
        migrations.AddField(
            model_name="coffeeshop",
            name="video",
            field=models.FileField(
                blank=True, null=True, upload_to="coffeeshop_videos"
            ),
        ),
    ]
