# Generated by Django 5.0.7 on 2024-07-17 01:46

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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "email",
                    models.EmailField(
                        help_text="Укажите электронную почту",
                        max_length=254,
                        unique=True,
                        verbose_name="Почта",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        help_text="Введите имя, макс 64 символа",
                        max_length=64,
                        verbose_name="Имя",
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        help_text="Введите фамилию, макс 64 символа",
                        max_length=64,
                        verbose_name="Фамилия",
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        help_text="Укажите телефон для связи",
                        max_length=15,
                        verbose_name="Телефон",
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        choices=[("user", "Пользователь"), ("admin", "Администратор")],
                        default="user",
                        help_text="Укажите роль",
                        max_length=5,
                        verbose_name="Роль",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        help_text="Разместите Вашу фотографию",
                        null=True,
                        upload_to="users/image",
                        verbose_name="Фотография",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Укажите активен ли пользователь",
                        verbose_name="Активация",
                    ),
                ),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
            ],
            options={
                "verbose_name": "Пользователя",
                "verbose_name_plural": "Пользователи",
                "ordering": ["email"],
            },
        ),
    ]
