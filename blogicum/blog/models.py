from django.db import models
from blogicum.core.models import PublishedModel
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(PublishedModel):
    title = models.CharField(
        'Название',
        max_length=256,
        help_text='Название категории, не более 256 символов, обязательное поле'
    )
    description = models.TextField(
        'Описание',
        help_text='Описание публикации, обязательное поле'
    )
    slug = models.SlugField(
        'Ссылка',
        max_length=64,
        unique=True,
        help_text='Уникальная ссылка на категорию, не более 256 символов, обязательное поле'
    )

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Location(PublishedModel):
    title = models.CharField(
        'Название',
        max_length=256,
        help_text='Название географической метки, не более 256 символов, обязательное поле'
    )

    class Meta:
        verbose_name = 'географическую метку'
        verbose_name_plural = 'Географические метки'

    def __str__(self):
        return self.title


class Post(PublishedModel):
    title = models.CharField(
        'Название',
        max_length=256,
        help_text='Название публикации, не более 256 символов, обязательное поле'
    )
    text = models.TextField(
        'Текст публикации',
        help_text='Текст публикации, обязательное поле'
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        help_text='Дата публикации, обязательное поле'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор'
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        related_name='posts',
        null=True,
        blank=True,
        verbose_name='Локация'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name='Категория'
    )

    class Meta:
        verbose_name = 'публикацию'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title


posts = [
    {
        'id': 0,
        'location': 'Остров отчаянья',
        'date': '30 сентября 1659 года',
        'category': 'travel',
        'text': '''Наш корабль, застигнутый в открытом море
                страшным штормом, потерпел крушение.
                Весь экипаж, кроме меня, утонул; я же,
                несчастный Робинзон Крузо, был выброшен
                полумёртвым на берег этого проклятого острова,
                который назвал островом Отчаяния.''',
    },
    {
        'id': 1,
        'location': 'Остров отчаянья',
        'date': '1 октября 1659 года',
        'category': 'not-my-day',
        'text': '''Проснувшись поутру, я увидел, что наш корабль сняло
                с мели приливом и пригнало гораздо ближе к берегу.
                Это подало мне надежду, что, когда ветер стихнет,
                мне удастся добраться до корабля и запастись едой и
                другими необходимыми вещами. Я немного приободрился,
                хотя печаль о погибших товарищах не покидала меня.
                Мне всё думалось, что, останься мы на корабле, мы
                непременно спаслись бы. Теперь из его обломков мы могли бы
                построить баркас, на котором и выбрались бы из этого
                гиблого места.''',
    },
    {
        'id': 2,
        'location': 'Остров отчаянья',
        'date': '25 октября 1659 года',
        'category': 'not-my-day',
        'text': '''Всю ночь и весь день шёл дождь и дул сильный
                порывистый ветер. 25 октября.  Корабль за ночь разбило
                в щепки; на том месте, где он стоял, торчат какие-то
                жалкие обломки,  да и те видны только во время отлива.
                Весь этот день я хлопотал  около вещей: укрывал и
                укутывал их, чтобы не испортились от дождя.''',
    },
]
