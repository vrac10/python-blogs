# Generated by Django 2.1.10 on 2019-07-20 02:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("gsoc", "0045_auto_20190719_1851")]

    operations = [
        migrations.CreateModel(
            name="SendEmail",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "to",
                    models.CharField(
                        blank=True,
                        help_text="Separate email with a comma",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "to_group",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("students", "Students"),
                            ("mentors", "Mentors"),
                            ("suborg_admins", "Suborg Admins"),
                            ("admins", "Admins"),
                            ("all", "All"),
                        ],
                        max_length=80,
                        null=True,
                    ),
                ),
                ("subject", models.CharField(max_length=255)),
                ("body", models.TextField()),
                (
                    "scheduler",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gsoc.Scheduler",
                    ),
                ),
            ],
        )
    ]