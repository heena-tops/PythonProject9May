# Generated by Django 4.1.7 on 2023-04-12 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Daily_shop_App", "0006_cart"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart", name="total", field=models.IntegerField(default=0),
        ),
    ]