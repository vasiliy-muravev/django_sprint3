from django.db import models


# Абстрактная PublishedModel модель
class PublishedModel(models.Model):
    is_published = models.BooleanField(
        default=True,
        help_text='Флаг публикации на сайте'
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
        help_text='Дата публикации может быть использована при сортировке'
    )

    class Meta:
        abstract = True
