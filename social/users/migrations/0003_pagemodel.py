# Generated by Django 4.2.11 on 2024-05-13 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_user_groups_alter_user_is_active_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="PageModel",
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
            ],
        ),
    ]