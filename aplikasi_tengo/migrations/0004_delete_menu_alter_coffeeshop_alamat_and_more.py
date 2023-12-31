# Generated by Django 4.2.3 on 2023-07-23 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aplikasi_tengo", "0003_remove_menu_coffee_shop_remove_menu_harga_and_more"),
    ]

    operations = [
        migrations.DeleteModel(name="Menu",),
        migrations.AlterField(
            model_name="coffeeshop",
            name="alamat",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="coffeeshop",
            name="contact",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="coffeeshop",
            name="gallery",
            field=models.ImageField(upload_to="coffee_shop_gallery/"),
        ),
        migrations.AlterField(
            model_name="coffeeshop",
            name="nama",
            field=models.CharField(max_length=100),
        ),
    ]
