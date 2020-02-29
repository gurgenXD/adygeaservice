from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from uuid import uuid1
from core.models import SEO


class Teacher(models.Model):
    name = models.CharField(max_length=250, verbose_name='Имя')
    work_exp = models.CharField(max_length=250, verbose_name='Стаж работы')
    teach_exp = models.CharField(max_length=250, verbose_name='Педагогический стаж')
    text = models.TextField(verbose_name='Описание')
    is_active = models.BooleanField(default=True, verbose_name='Показывать на сайте')
    created = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def get_picture_url(self, filename):
        ext = filename.split('.')[-1]
        filename = '{0}.{1}'.format(uuid1(), ext)
        return 'images/teachers/{0}'.format(filename)

    image = models.ImageField(upload_to=get_picture_url, verbose_name='Фото')

    image_admin = ImageSpecField(source='image',
                                 processors=[ResizeToFill(150, 150)],
                                 format='JPEG',
                                 options={'quality': 90})

    image_small = ImageSpecField(source='image',
                                 processors=[ResizeToFill(64, 64)],
                                 format='JPEG',
                                 options={'quality': 90})

    def image_tag(self):
        try:
            image_link = self.image_admin.url
        except:
            image_link = ''
        return mark_safe('<a href="{0}"><img src="{0}" width="150px"></a>'.format(image_link))
    image_tag.short_description = 'Предпросмотр изоражения'
    image_tag.allow_tags = True

    def image_tag_mini(self):
        try:
            image_link = self.image_admin.url
        except:
            image_link = ''
            print(image_link)
        return mark_safe('<img src="{0}" width="53px">'.format(image_link))
    image_tag_mini.short_description = 'Предпросмотр'
    image_tag_mini.allow_tags = True

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'
        ordering = ('created',)

    def __str__(self):
        return self.name


class Direction(SEO):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    desc = models.TextField(verbose_name='Описание')
    is_active = models.BooleanField(default=True, verbose_name='Показывать на сайте')
    created_date = models.DateField(auto_now_add=True, verbose_name='Дата публикации')

    def get_picture_url(self, filename):
        ext = filename.split('.')[-1]
        filename = '{0}.{1}'.format(self.slug, ext)
        return 'images/directions/{0}'.format(filename)

    image = models.ImageField(upload_to=get_picture_url, verbose_name='Изображение')
    
    image_small = ImageSpecField(source='image',
                                     processors=[ResizeToFill(460, 170)],
                                     format='JPEG',
                                     options={'quality': 90})

    def get_absolute_url(self):
        return reverse('direction', args=[self.slug])

    class Meta:
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'
        ordering = ('created_date',)

    def __str__(self):
        return self.title


class Course(SEO):
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE, verbose_name='Курс', related_name='courses')
    teachers = models.ManyToManyField(Teacher, verbose_name='Преподаватели', related_name='courses')
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    duration = models.CharField(max_length=250, verbose_name='Длительность')
    course_reg = models.CharField(max_length=250, verbose_name='Запись на курс')
    price = models.CharField(max_length=250, verbose_name='Цена')
    desc = models.TextField(verbose_name='Описание')
    created_date = models.DateField(auto_now_add=True, verbose_name='Дата публикации')

    def get_absolute_url(self):
        return reverse('course', args=[self.slug])

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.title
