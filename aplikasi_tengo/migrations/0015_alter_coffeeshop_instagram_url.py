# Generated by Django 4.2.3 on 2023-08-06 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aplikasi_tengo", "0014_coffeeshop_google_maps_url_delete_menu"),
    ]

    operations = [
        migrations.AlterField(
            model_name="coffeeshop",
            name="instagram_url",
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
