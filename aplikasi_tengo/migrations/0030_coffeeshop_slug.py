# Generated by Django 4.2.3 on 2023-09-10 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aplikasi_tengo", "0029_remove_coffeeshop_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="coffeeshop",
            name="slug",
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
