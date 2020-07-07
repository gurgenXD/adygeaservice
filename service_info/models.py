from django.db import models
from core.models import SEO
from django.urls import reverse
from uuid import uuid1


class Document(models.Model):
    title = models.TextField(unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=250, verbose_name='Slug', unique=True)

    def get_document_url(self, filename):
        ext = filename.split('.')[-1]
        filename = '{0}.{1}'.format(uuid1(), ext)
        return 'documents/{0}'.format(filename)

    document = models.FileField(upload_to=get_document_url, max_length=254, verbose_name='Файл')

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    def __str__(self):
        return self.title


class Execution(models.Model):
    title = models.TextField(unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=250, verbose_name='Slug', unique=True)

    def get_document_url(self, filename):
        ext = filename.split('.')[-1]
        filename = '{0}.{1}'.format(uuid1(), ext)
        return 'executions/{0}'.format(filename)

    document = models.FileField(upload_to=get_document_url, max_length=254, verbose_name='Файл')

    class Meta:
        verbose_name = 'Информация во исполнение'
        verbose_name_plural = 'Информация во исполнение'

    def __str__(self):
        return self.title


class Structure(SEO):
    title = models.TextField(verbose_name='Название')
    table_info = models.TextField(verbose_name='Текст')

    class Meta:
        verbose_name = 'Структура и органы управления образовательной организацией'
        verbose_name_plural = 'Структуры и органы управления образовательной организацией'

    def get_absolute_url(self):
        return reverse('structure', args=[self.slug])

    def __str__(self):
        return 'Структура и органы управления образовательной организацией №{0}'.format(self.id)


class Info(models.Model):
    info = models.TextField(verbose_name='Основные сведения')

    class Meta:
        verbose_name = 'Основные сведения'
        verbose_name_plural = 'Основные сведения'

    def __str__(self):
        return 'Основные сведения №{0}'.format(self.id)
