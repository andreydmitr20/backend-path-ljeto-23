# Generated by Django 4.1.7 on 2023-03-26 20:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bands", "0003_band_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="band",
            name="image",
            field=models.URLField(blank=True, default=""),
        ),
    ]
