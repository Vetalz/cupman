# Generated by Django 3.2.8 on 2021-10-24 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method_delivery', models.CharField(choices=[('1', 'Доставка по Украине'), ('2', 'Самовывоз в Кривом Роге')], default=('1', 'Доставка по Украине'), max_length=300, verbose_name='Метод доставки')),
                ('name', models.CharField(max_length=300, verbose_name='ФИО')),
                ('phone', models.CharField(max_length=13, verbose_name='Номер телефона')),
                ('region', models.CharField(blank=True, choices=[('02', 'Вінницька область'), ('03', 'Волинська область'), ('04', 'Дніпропетровська область'), ('05', 'Донецька область'), ('06', 'Житомирська область'), ('07', 'Закарпатська область'), ('08', 'Запорізька область'), ('09', 'Івано-Франківська область'), ('10', 'Київська область'), ('11', 'Київ'), ('12', 'Кіровоградська область'), ('13', 'Луганська область'), ('14', 'Львівська область'), ('15', 'Миколаївська область'), ('16', 'Одеська область'), ('17', 'Полтавська область'), ('18', 'Рівненська область'), ('19', 'Сумська область'), ('20', 'Тернопільська область'), ('21', 'Харківська область'), ('22', 'Херсонська область'), ('23', 'Хмельницька область'), ('24', 'Черкаська область'), ('26', 'Чернівецька область'), ('25', 'Чернігівська область')], max_length=100, verbose_name='Область')),
                ('city', models.CharField(blank=True, max_length=100, verbose_name='Город')),
                ('new_post_office', models.CharField(choices=[('1', 'Моментальная онлайн оплата'), ('2', 'Оплата после консультации')], default=('1', 'Моментальная онлайн оплата'), max_length=300, verbose_name='Отделение Новой Почты')),
                ('address', models.CharField(blank=True, max_length=300, verbose_name='Адрес')),
                ('comment', models.TextField(blank=True, verbose_name='Комментарий')),
                ('method_payment', models.CharField(choices=[('1', 'Моментальная онлайн оплата'), ('2', 'Оплата после консультации')], default=('1', 'Моментальная онлайн оплата'), max_length=300, verbose_name='Метод оплаты')),
                ('product', models.JSONField(verbose_name='Товары')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('status', models.CharField(choices=[('1', 'Новый'), ('2', 'В обработке'), ('3', 'Доставляется'), ('4', 'Успешный'), ('5', 'Неуспешный')], default=('1', 'Новый'), max_length=100)),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_updated', models.DateField(auto_now=True, verbose_name='Дата обновления')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('popular', models.BooleanField(verbose_name='Популярный')),
                ('new', models.BooleanField(verbose_name='Новинка')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('main_image', models.ImageField(upload_to='coffee/%Y/%m/%d/', verbose_name='Фото')),
                ('qty', models.PositiveIntegerField(verbose_name='Количество')),
                ('options', models.JSONField(verbose_name='Параметры')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='shop.category', verbose_name='Категория')),
                ('related_product', models.ManyToManyField(blank=True, related_name='_shop_product_related_product_+', to='shop.Product', verbose_name='Связанные продукты')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
