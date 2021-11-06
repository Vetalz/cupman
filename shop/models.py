import uuid
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='product', verbose_name='Категория')
    popular = models.BooleanField(verbose_name='Популярный')
    new = models.BooleanField(verbose_name='Новинка')
    sale_percent = models.PositiveIntegerField(verbose_name='Скидка, %', null=True, blank=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    main_image = models.ImageField(upload_to='coffee/%Y/%m/%d/', verbose_name='Фото')
    related_product = models.ManyToManyField('self', verbose_name='Связанные продукты', blank=True)
    qty = models.PositiveIntegerField(verbose_name='Количество')
    options = models.JSONField(verbose_name='Параметры')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('coffee_detail', args=[str(self.slug)])


REGION_CHOICES = (
    ('02', 'Вінницька область'),
    ('03', 'Волинська область'),
    ('04', 'Дніпропетровська область'),
    ('05', 'Донецька область'),
    ('06', 'Житомирська область'),
    ('07', 'Закарпатська область'),
    ('08', 'Запорізька область'),
    ('09', 'Івано-Франківська область'),
    ('10', 'Київська область'),
    ('11', 'Київ'),
    ('12', 'Кіровоградська область'),
    ('13', 'Луганська область'),
    ('14', 'Львівська область'),
    ('15', 'Миколаївська область'),
    ('16', 'Одеська область'),
    ('17', 'Полтавська область'),
    ('18', 'Рівненська область'),
    ('19', 'Сумська область'),
    ('20', 'Тернопільська область'),
    ('21', 'Харківська область'),
    ('22', 'Херсонська область'),
    ('23', 'Хмельницька область'),
    ('24', 'Черкаська область'),
    ('26', 'Чернівецька область'),
    ('25', 'Чернігівська область'),
)

DELIVERY_CHOICES = (
    ('1', 'Доставка по Украине'),
    ('2', 'Самовывоз в Кривом Роге')
)

PAYMENT_CHOICES = (
    ('1', 'Моментальная онлайн оплата'),
    ('2', 'Оплата после консультации')
)


ORDER_STATUS = (
    ('1', 'Новый'),
    ('2', 'В обработке'),
    ('3', 'Доставляется'),
    ('4', 'Успешный'),
    ('5', 'Неуспешный'),
)


class Order(models.Model):
    method_delivery = models.CharField(choices=DELIVERY_CHOICES, max_length=300, default=DELIVERY_CHOICES[0],
                                       verbose_name='Метод доставки')
    name = models.CharField(max_length=300, verbose_name='ФИО')
    phone = models.CharField(max_length=13, verbose_name='Номер телефона')
    region = models.CharField(max_length=100, choices=REGION_CHOICES, blank=True, verbose_name='Область', default=REGION_CHOICES[2])
    city = models.CharField(max_length=100, verbose_name='Город', blank=True)
    new_post_office = models.CharField( max_length=300, verbose_name='Отделение Новой Почты', blank=True)
    address = models.CharField(max_length=300, blank=True, verbose_name='Адрес')
    comment = models.TextField(blank=True, verbose_name='Комментарий')
    method_payment = models.CharField(choices=PAYMENT_CHOICES, max_length=300, default=PAYMENT_CHOICES[0],
                                      verbose_name='Метод оплаты')
    product = models.JSONField(verbose_name='Товары')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    status = models.CharField(max_length=100, choices=ORDER_STATUS, default=ORDER_STATUS[0])
    date_created = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    date_updated = models.DateField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return self.phone












