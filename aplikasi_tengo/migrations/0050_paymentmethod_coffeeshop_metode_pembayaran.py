# Generated by Django 5.1.1 on 2024-09-15 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplikasi_tengo', '0049_remove_coffeeshop_menu_image_coffeeshop_menu_images_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_metode', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='coffeeshop',
            name='metode_pembayaran',
            field=models.ManyToManyField(blank=True, to='aplikasi_tengo.paymentmethod'),
        ),
    ]