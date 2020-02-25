from django.db import models
# from contacts.models import Phone, Address


class SEO(models.Model):
    seo_title = models.CharField(max_length=250, verbose_name='Title', null=True, blank=True)
    seo_desc = models.CharField(max_length=250, verbose_name='Description', null=True, blank=True)
    seo_kwrds = models.CharField(max_length=250, verbose_name='Keywords', blank=True)
    slug = models.SlugField(max_length=250, verbose_name='Slug', unique=True)

    class Meta:
        abstract = True


class Position(models.Model):
    position = models.PositiveIntegerField(verbose_name='Позиция', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.position is None:
            try:
                last = self.objects.order_by('-position')[0]
                self.position = last.position + 1
            except:
                self.position = 0
        return super(Position, self).save(*args, **kwargs)

    class Meta:
        abstract = True
        ordering = ('position',)


class MailToString(models.Model):
    email = models.EmailField(max_length=250, verbose_name='E-mail')

    class Meta:
        verbose_name = 'Кому отправлять письмо'
        verbose_name_plural = 'Кому отправлять письмо'

    def __str__(self):
        return self.email


class MailFromString(models.Model):
    use_tls = models.BooleanField(verbose_name='EMAIL_USE_TLS(gmail.com, mail.ru)')
    use_ssl = models.BooleanField(verbose_name='EMAIL_USE_SSL(yandex.ru)')
    port = models.PositiveIntegerField(verbose_name='EMAIL_PORT')
    host = models.CharField(max_length=250, verbose_name='EMAIL_HOST')
    host_user = models.EmailField(max_length=250, verbose_name='EMAIL_HOST_USER')
    host_password = models.CharField(max_length=250, verbose_name='EMAIL_HOST_PASSWORD')

    class Meta:
        verbose_name = 'Откуда отправлять письмо'
        verbose_name_plural = 'Откуда отправлять письмо'

    def __str__(self):
        return self.host_user


class TitleTag(models.Model):
    url = models.CharField(max_length=250, verbose_name='URL')
    seo_title = models.CharField(max_length=250, verbose_name='Title', null=True, blank=True)
    seo_desc = models.CharField(max_length=250, verbose_name='Description', null=True, blank=True)
    seo_kwrds = models.CharField(max_length=250, verbose_name='Keywords', null=True, blank=True)

    class Meta:
        verbose_name = 'SEO title'
        verbose_name_plural = 'SEO titles'

    def __str__(self):
        return self.seo_title
#
#
# class Index(models.Model):
#     phone = models.ForeignKey(Phone, on_delete=models.SET_NULL, verbose_name='Телефон', null=True)
#     address = models.ForeignKey(Address, on_delete=models.SET_NULL, verbose_name='Адрес', null=True)
#     service = models.ForeignKey(Service, on_delete=models.SET_NULL, verbose_name='Услуга', null=True)
#     about = models.TextField(verbose_name='О нас')
#
#     class Meta:
#         verbose_name = 'Главная страница'
#         verbose_name_plural = 'Главная страница'
#
#     def __str__(self):
#         return 'Главная страница #{0}'.format(self.id)
#
#
# class Slide(models.Model):
#     index = models.ForeignKey(Index, on_delete=models.CASCADE, verbose_name='Главная', related_name='slides')
#     title = models.CharField(max_length=250, verbose_name='Заголовок')
#     desc = models.CharField(max_length=250, verbose_name='Описание')
#     image = models.ImageField(upload_to='index/slides/', verbose_name='Фото')
#
#     class Meta:
#         verbose_name = 'Слайд'
#         verbose_name_plural = 'Слайды'
#
#     def __str__(self):
#         return self.title
#
#
# class Fact(models.Model):
#     index = models.ForeignKey(Index, on_delete=models.CASCADE, verbose_name='Главная', related_name='facts')
#     top = models.CharField(max_length=10, verbose_name='Вверх')
#     center = models.CharField(max_length=250, verbose_name='Центр')
#     bottom = models.CharField(max_length=250, verbose_name='Низ')
#
#     class Meta:
#         verbose_name = 'Факт'
#         verbose_name_plural = 'Факты'
#
#     def __str__(self):
#         return self.center
#
#
# class Partner(models.Model):
#     index = models.ForeignKey(Index, on_delete=models.CASCADE, verbose_name='Главная', related_name='partners')
#     url = models.URLField(max_length=250, verbose_name='URL')
#     image = models.ImageField(upload_to='index/partners/', verbose_name='Фото')
#
#     class Meta:
#         verbose_name = 'Партнёр'
#         verbose_name_plural = 'Партнёры'
#
#     def __str__(self):
#         return self.url
#
#
# class Goal(models.Model):
#     index = models.ForeignKey(Index, on_delete=models.CASCADE, verbose_name='Главная', related_name='goals')
#     title = models.CharField(max_length=250, verbose_name='Заголовок')
#     text = models.CharField(max_length=250, verbose_name='Текст')
#     image = models.ImageField(upload_to='index/goals/', verbose_name='Фото')
#
#     class Meta:
#         verbose_name = 'Преимущество'
#         verbose_name_plural = 'Преимущества'
#
#     def __str__(self):
#         return self.title
