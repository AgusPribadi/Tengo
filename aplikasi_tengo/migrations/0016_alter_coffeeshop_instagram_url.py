# Generated by Django 4.2.3 on 2023-08-06 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aplikasi_tengo", "0015_alter_coffeeshop_instagram_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="coffeeshop",
            name="instagram_url",
            field=models.URLField(blank=True, null=True),
        ),
    ]
