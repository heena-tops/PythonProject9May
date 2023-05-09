# Generated by Django 4.1.7 on 2023-03-20 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("fname", models.CharField(max_length=100)),
                ("lname", models.CharField(max_length=100)),
                ("DOB", models.DateTimeField(blank=True, default="")),
                ("email", models.EmailField(max_length=254)),
                ("contact", models.IntegerField()),
                ("password", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=100)),
            ],
        ),
    ]