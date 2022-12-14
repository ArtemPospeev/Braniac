# Generated by Django 4.1.3 on 2022-12-01 23:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("mainapp", "0003_alter_courseteachers_options_alter_courses_cost_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="CourseFeedback",
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
                    models.DateTimeField(auto_now_add=True, verbose_name="Создан"),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now=True, verbose_name="Обновлен"),
                ),
                ("deleted", models.BooleanField(default=False, verbose_name="Удален")),
                (
                    "rating",
                    models.SmallIntegerField(
                        choices=[
                            (5, "⭐⭐⭐⭐⭐"),
                            (4, "⭐⭐⭐⭐"),
                            (3, "⭐⭐⭐"),
                            (2, "⭐⭐"),
                            (1, "⭐"),
                        ],
                        default=5,
                        verbose_name="Рейтинг",
                    ),
                ),
                (
                    "feedback",
                    models.TextField(default="Без отзыва", verbose_name="Отзыв"),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mainapp.courses",
                        verbose_name="Курс",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Отзыв",
                "verbose_name_plural": "Отзывы",
            },
        ),
    ]
