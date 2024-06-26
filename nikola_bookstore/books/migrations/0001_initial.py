# Generated by Django 5.0.4 on 2024-04-17 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=200)),
                ("author", models.CharField(max_length=100)),
                ("year", models.IntegerField()),
                ("rating", models.DecimalField(decimal_places=1, max_digits=3)),
                ("description", models.TextField()),
            ],
        ),
    ]
