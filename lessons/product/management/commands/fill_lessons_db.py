import csv

from django.core.management import BaseCommand

from product.models import Lesson


class Command(BaseCommand):
    """
    Наполнение базы данных данными из lessons.csv .
    Команда - python manage.py fill_lessons_db.
    """
    def handle(self, *args, **options):

        file_path = 'data/lessons.csv'
        print('Загрузка началась')

        with open(file_path, 'r', encoding='utf-8') as csv_file:
            lessons = csv.reader(csv_file)

            for row in lessons:
                name, video_link, duration = row
                Lesson.objects.get_or_create(
                    name=name,
                    video_link=video_link,
                    duration=duration
                )

        print('Загрузка успешно завершена')
