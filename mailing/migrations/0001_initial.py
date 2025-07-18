# Generated by Django 5.2.1 on 2025-06-08 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AttemptMailing",
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
                    "date_attempt",
                    models.DateTimeField(verbose_name="Дата и время попытки"),
                ),
                (
                    "status",
                    models.CharField(max_length=115, verbose_name="Статус попытки"),
                ),
                (
                    "response",
                    models.TextField(blank=True, null=True, verbose_name="Комментарии"),
                ),
            ],
            options={
                "verbose_name": "попытка",
                "verbose_name_plural": "попытки",
                "ordering": ["date_attempt", "status"],
            },
        ),
        migrations.CreateModel(
            name="Mailing",
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
                    "first_sending",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Дата первой отправки"
                    ),
                ),
                (
                    "end_sending",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Дата окончания отправки"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Создано", "Создано"),
                            ("Запущено", "Запущено"),
                            ("Завершена", "Завершена"),
                        ],
                        default="Создано",
                        max_length=11,
                        verbose_name="Статус рассылки",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        blank=True, default=True, null=True, verbose_name="активна"
                    ),
                ),
            ],
            options={
                "verbose_name": "Рассылка",
                "verbose_name_plural": "Рассылки",
                "ordering": ["first_sending"],
                "permissions": [("set_is_active", "set is active")],
            },
        ),
        migrations.CreateModel(
            name="Message",
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
                    "subject",
                    models.CharField(max_length=255, verbose_name="Тема письма"),
                ),
                ("content", models.TextField(verbose_name="Содержимое письма")),
            ],
            options={
                "verbose_name": "письмо",
                "verbose_name_plural": "письма",
                "ordering": ["subject"],
                "permissions": [("can_blocking_sms", "Может блокировать сообщение")],
            },
        ),
        migrations.CreateModel(
            name="ReceiveMail",
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
                    "mail",
                    models.EmailField(
                        max_length=255, unique=True, verbose_name="Письмо"
                    ),
                ),
                ("fio", models.CharField(max_length=255, verbose_name="ФИО")),
                (
                    "comment",
                    models.TextField(blank=True, null=True, verbose_name="Комментарии"),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="активность"),
                ),
            ],
            options={
                "verbose_name": "получатель",
                "verbose_name_plural": "получатели",
                "ordering": ["fio"],
                "permissions": [
                    ("can_blocking_client", "Может блокировать получателя")
                ],
            },
        ),
    ]
