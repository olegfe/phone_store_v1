from django.db import models
from django.core.urlresolvers import reverse
from django.contrib import admin
from datetime import datetime
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                        args=[self.slug])

    def __str__(self):
        return self.name

admin.site.register(Category)


class Product(models.Model):
    #ОБЩИЕ ХАРАКТЕРИСТИКИ 
    category = models.ForeignKey(Category, related_name='products')
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True)
    image1 = models.FileField(upload_to='products/%Y/%m/%d', blank=True, verbose_name = "Картинка_1")
    image2 = models.FileField(upload_to='products/%Y/%m/%d', blank=True, verbose_name = "Картинка_2")
    image3 = models.FileField(upload_to='products/%Y/%m/%d', blank=True, verbose_name = "Картинка_3")


    case_type = models.CharField (max_length = 255 ,default = False, verbose_name = "Тип корпуса")
    duo_sim = models.BooleanField (default = True, verbose_name = "Поддержка двух сим карт")
    sim_type = models.CharField(max_length=255, default="input", verbose_name = "Тип SIM-карты")
    system= models.CharField(max_length = 100, default = "system", verbose_name = "Операционная система")

    #ДИСПЛЕЙ

    display_type = models.CharField(max_length = 10, default = False, verbose_name = "Тип экрана")
    resolution = models.CharField(max_length = 20,default = False , verbose_name = "Разрешение экрана")

    #КОНФИГУРАЦИЯ
    processor = models.CharField(max_length = 255, default = False, verbose_name = "Процессор")
    gpu = models.CharField(max_length = 255, default = False, verbose_name = "Графический ускроритель")
    cores = models.CharField(max_length = 5, default = False, verbose_name = "Кол-во ядер")
    cpu_frequency = models.CharField(max_length = 5,  verbose_name= "Частота процессора")
    ram = models.CharField(max_length=255, verbose_name='Объем оперативной памяти')
    ram_inside = models.CharField(max_length = 255,  verbose_name = "Объем встроенной памяти")
    sd = models.BooleanField(default=True, verbose_name='Наличие SD карты')
    sd_volume_max = models.CharField(max_length=255, blank=True, null=True, verbose_name='Максимальный объем SD карты')

    #КАМЕРА
    main_cam_mp = models.CharField(max_length=255, verbose_name='Основная камера')
    frontal_cam_mp = models.CharField(max_length=255, verbose_name='Фронтальная камера')
    flash = models.BooleanField(default=True, verbose_name = "Вспышка")

    #МУЛЬТИМЕДИА

    mp3_pleer = models.BooleanField(default=True, verbose_name="MP3 плеер")
    recorder = models.BooleanField(default=True, verbose_name="Диктофон")
    usb_interface = models.CharField (max_length = 255, verbose_name = "Интерфейс USB")

    #ПИТАНИЕ

    accum_volume = models.CharField(max_length=255, verbose_name='Объем батареи мА*ч ')
    
   
    #КОПРУС

    size = models.CharField(max_length=255, verbose_name = "Размеры (ШхВхТ)")
    weigth = models.CharField(max_length = 10, verbose_name = "Вес г.")
    
    description = models.TextField(blank=True)
    country = models.CharField(max_length= 255, verbose_name = "Страна производителя")
    warranty  = models.CharField(max_length= 255, verbose_name = "Гарантия")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                        args=[self.id, self.slug])

    def __str__(self):
        return self.name


admin.site.register(Product)



class Review(models.Model):  #Отзывы о товаре
    product = models.ForeignKey(Product, on_delete = models.CASCADE, verbose_name = "Продукт")
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "Автор")
    plus = models.CharField(max_length= 2000,blank=False,verbose_name = 'Достоинства')
    minus = models.CharField(max_length = 2000,blank=False, verbose_name = 'Недоститки')
    comment = models.CharField(max_length = 5000,blank=False, verbose_name = 'Комментарий')
    date = models.DateTimeField(default = datetime.now(),db_index = True, verbose_name = "Дата")

    

    def __str__(self):
       return 'Отзыв %s к %s' %(self.author, self.product)

    class Meta:
        db_table = "Отзывы" # имя таблицы для модели
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзыв к продукту"
        ordering= ["-date"]

admin.site.register(Review)
