# Generated by Django 4.1.7 on 2023-04-20 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Daily_shop_App", "0008_cart_net_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="razorpay_order_id",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="cart",
            name="razorpay_payment_id",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="cart",
            name="razorpay_payment_signature",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
