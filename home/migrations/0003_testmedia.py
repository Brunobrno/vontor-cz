# Generated by Django 5.1.3 on 2024-11-29 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_rename_message_anonmessage_text"),
    ]

    operations = [
        migrations.CreateModel(
            name="TestMedia",
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
                ("file", models.FileField(upload_to="")),
            ],
        ),
    ]