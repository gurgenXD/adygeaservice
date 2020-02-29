from django.db import models
from directions.models import  Course


class Order(models.Model):
    name = models.CharField(max_length=250, verbose_name='Имя')
    email_or_phone = models.CharField(max_length=250, verbose_name='E-mail или телефон')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', related_name='orders')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время заявки')

    class Meta:
        verbose_name = 'Запись на курс'
        verbose_name_plural = 'Записи на курсы'

    def __str__(self):
        return '{0} ({1})'.format(self.name, self.email_or_phone)
