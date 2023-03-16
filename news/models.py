from django.db import models

"""
В файле моделс создаются классы, наследуемые от класса models.Model
Это нужно для работы с базами данных. Классы являются таблицами.
Каждая переменная внутри класса является строкой в таблице.
После создание класса и описания строк нужно выполнить миграции.
Миграции - синхронизация приложения/проекта с базами данных.
python manage.py makemigrations
python manage.py migrate
Далее таблицу нужно зарегестрировать в news/admin.py

Вложенный класс Мета нужен для корректного отображения названий таблиц
на сайте
"""


class Articles(models.Model):
    title = models.CharField('Name', max_length=50, )
    intro = models.CharField('Introduction', max_length=250, )
    text_content = models.TextField('Actual')
    date = models.DateTimeField('Publication date')

    def __str__(self):
        return self.title
        # Метод показывает как именно нужно выводить объекты в шаблоне

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
