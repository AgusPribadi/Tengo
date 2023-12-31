# Generated by Django 4.2.3 on 2023-08-20 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("aplikasi_tengo", "0016_alter_coffeeshop_instagram_url"),
    ]

    operations = [
        migrations.CreateModel(
            name="CoffeeShopImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="coffeeshop_images")),
                (
                    "coffee_shop",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="aplikasi_tengo.coffeeshop",
                    ),
                ),
            ],
        ),
    ]
