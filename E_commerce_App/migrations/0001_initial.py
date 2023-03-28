# Generated by Django 4.1.3 on 2022-12-29 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cartmodel",
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
                ("userID", models.IntegerField()),
                ("productID", models.IntegerField()),
                ("orderID", models.IntegerField(default=0)),
                ("productname", models.CharField(max_length=220)),
                ("productprice", models.IntegerField()),
                ("productimage", models.ImageField(default="", upload_to="Cartimage")),
                ("Quantity", models.IntegerField(default=2)),
            ],
        ),
        migrations.CreateModel(
            name="Catogerymodel",
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
                ("Catogery_name", models.CharField(max_length=220)),
                ("Catogery_img", models.ImageField(default="", upload_to="Catogery")),
            ],
        ),
        migrations.CreateModel(
            name="faviourate_model",
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
                ("userId", models.IntegerField()),
                ("productID", models.IntegerField()),
                ("pro_name", models.CharField(max_length=220)),
                ("pro_img", models.ImageField(upload_to="fav")),
                ("pro_dec", models.CharField(max_length=220)),
                ("pro_price", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Shipingmodel",
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
                ("userId", models.IntegerField()),
                ("username", models.CharField(max_length=200)),
                ("userEmail", models.EmailField(max_length=254)),
                ("usercontect", models.IntegerField()),
                ("Address", models.TextField()),
                ("Area", models.CharField(max_length=20)),
                ("City", models.CharField(max_length=20)),
                ("Pincode", models.BigIntegerField()),
                ("Payment_Type", models.CharField(max_length=20)),
                ("Date_time", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="sub_catogerymodel",
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
                ("sub_Catogery_name", models.CharField(max_length=220)),
                (
                    "sub_Catogery_img",
                    models.ImageField(default="", upload_to="Sub_Catogery"),
                ),
                (
                    "Catogery",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="E_commerce_App.catogerymodel",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Productmodel",
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
                ("Product_name", models.CharField(max_length=2000)),
                ("Product_price", models.IntegerField()),
                ("Product_dec", models.TextField()),
                ("img", models.ImageField(default="", upload_to="Product")),
                (
                    "sub_catogery",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="E_commerce_App.sub_catogerymodel",
                    ),
                ),
            ],
        ),
    ]
