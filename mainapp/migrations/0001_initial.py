# Generated by Django 4.1.3 on 2022-11-30 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Courses",
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
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created"),
                ),
                ("updated", models.DateTimeField(auto_now=True, verbose_name="Edited")),
                ("deleted", models.BooleanField(default=False)),
                ("name", models.CharField(max_length=256, verbose_name="Name")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
                ),
                (
                    "description_as_markdown",
                    models.BooleanField(default=False, verbose_name="As markdown"),
                ),
                (
                    "cost",
                    models.DecimalField(
                        decimal_places=2, default=0, max_digits=8, verbose_name="Cost"
                    ),
                ),
                (
                    "cover",
                    models.CharField(
                        default="no_image.svg", max_length=25, verbose_name="Cover"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="News",
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
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created"),
                ),
                ("updated", models.DateTimeField(auto_now=True, verbose_name="Edited")),
                ("deleted", models.BooleanField(default=False)),
                ("title", models.CharField(max_length=128, verbose_name="Title")),
                (
                    "preambule",
                    models.CharField(max_length=1024, verbose_name="Preambule"),
                ),
                ("body", models.TextField(blank=True, null=True, verbose_name="Body")),
                (
                    "body_as_markdown",
                    models.BooleanField(default=False, verbose_name="As markdown"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Lesson",
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
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created"),
                ),
                ("updated", models.DateTimeField(auto_now=True, verbose_name="Edited")),
                ("deleted", models.BooleanField(default=False)),
                ("num", models.PositiveIntegerField(verbose_name="Lesson number")),
                ("title", models.CharField(max_length=256, verbose_name="Name")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
                ),
                (
                    "description_as_markdown",
                    models.BooleanField(default=False, verbose_name="As markdown"),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mainapp.courses",
                    ),
                ),
            ],
            options={
                "ordering": ("course", "num"),
            },
        ),
        migrations.CreateModel(
            name="CourseTeachers",
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
                ("name_first", models.CharField(max_length=128, verbose_name="Name")),
                (
                    "name_second",
                    models.CharField(max_length=128, verbose_name="Surname"),
                ),
                ("day_birth", models.DateField(verbose_name="Birth date")),
                ("deleted", models.BooleanField(default=False)),
                ("course", models.ManyToManyField(to="mainapp.courses")),
            ],
        ),
    ]
