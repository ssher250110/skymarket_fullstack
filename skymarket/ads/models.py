from django.conf import settings
from django.db import models

NULLABLE = {"null": True, "blank": True}


class Ad(models.Model):
    """ Модель объявления """

    title = models.CharField(max_length=50, verbose_name="Название товара", help_text="Укажите название товара")
    description = models.TextField(**NULLABLE, verbose_name="Описание товара", help_text="Укажите описание товара")
    price = models.PositiveIntegerField(verbose_name="Цена товара", help_text="Укажите цену товара")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания объявления")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE,
                               verbose_name="Автор объявления", help_text="Укажите автора объявления")
    image = models.ImageField(upload_to="ad/image", **NULLABLE, verbose_name="Изображение",
                              help_text="Загрузите изображение")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ["-created_at"]


class Comment(models.Model):
    """ Модель отзыва """

    text = models.TextField(verbose_name="Текст отзыва", help_text="Добавьте текст отзыва")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE,
                               verbose_name="Автор отзыва", help_text="Укажите автора отзыва")
    ad = models.ForeignKey("Ad", on_delete=models.CASCADE, verbose_name="Объявление", help_text="Укажите объявление")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания отзыва")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
