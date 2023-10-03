from django.contrib import admin

from .models import Lesson, Product, ProductLessons, LessonStatus


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'video_link', 'duration')
    list_filter = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'author')
    list_filter = ('name',)


@admin.register(ProductLessons)
class ProductLessonsAdmin(admin.ModelAdmin):
    list_display = ('product', 'lessons')


@admin.register(LessonStatus)
class LessonStatusAdmin(admin.ModelAdmin):
    list_display = ('user', 'lesson', 'duration')
