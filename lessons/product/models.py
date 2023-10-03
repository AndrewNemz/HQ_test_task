from django.db import models

from users.models import CustomUser


class Lesson(models.Model):
    '''
    Модель для уроков.
    '''
    name = models.CharField(
        verbose_name='Название урока',
        max_length=200,
    )
    video_link = models.URLField(
        verbose_name='Ссылка на видеоурок',
        max_length=200,
    )
    duration = models.DurationField(
        verbose_name='Длительность видео'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return self.name


class Product(models.Model):
    '''
    Модель для продукта.
    У каждого продукта есть автор.
    '''
    name = models.CharField(
        verbose_name='Имя продукта',
        max_length=200
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='product',
        verbose_name='Автор продукта',
    )
    lesson = models.ManyToManyField(
        Lesson,
        through='ProductLessons',
        verbose_name='Уроки продукта'
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)

    def __str__(self):
        return self.name


class ProductLessons(models.Model):
    '''
    Модель для уроков, из которых состоит продукт.
    '''

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='lessons_amount',
        verbose_name='Продукт',
    )
    lessons = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name='lessons_amount',
        verbose_name='Урок',
    )

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('product', 'lessons',),
                name='unique_ingredient',
            ),
        )
        verbose_name = 'Количество уроков'
        ordering = ['-id']

    def __str__(self):
        return self.lessons.name


class LessonStatus(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='stat'
        )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        verbose_name='Урок',
        related_name='stat'
    )
    duration = models.DurationField()
    last_time_watched = models.DateTimeField(auto_now_add=True)
