# Generated by Django 4.1.7 on 2023-04-03 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Daily_shop_App", "0003_category_product"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="product_image",
            field=models.ImageField(upload_to="product_image/"),
        ),
    ]
