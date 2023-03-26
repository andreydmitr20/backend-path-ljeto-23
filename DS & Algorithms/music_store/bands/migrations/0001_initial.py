# Generated by Django 4.1.7 on 2023-03-26 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Band",
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
                ("name", models.CharField(max_length=200)),
                ("can_rock", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="Member",
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
                (
                    "name",
                    models.CharField(max_length=200, verbose_name="member's name"),
                ),
                (
                    "instruments",
                    models.CharField(
                        choices=[("g", "Guitar"), ("b", "Bass"), ("d", "Drum")],
                        max_length=1,
                    ),
                ),
                (
                    "band",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="bands.band"
                    ),
                ),
            ],
        ),
    ]
