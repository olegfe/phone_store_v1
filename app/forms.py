"""
Definition of forms.
"""

from django import forms
from django.db import models
from .models import Comment
from .models import Blog, Contact
from django.contrib.auth.models import User
import datetime
from shop.models import Product

from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Логин'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))


class AnketaForm(forms.Form):
    name = forms.CharField(label = 'Ваше имя', min_length = 2, max_length = 100)
    city = forms.CharField(label = 'Ваш город', min_length = 2, max_length=100)
    job = forms.CharField(label = 'Ваш род занятий', min_length = 2, max_length = 100)
    gender = forms.ChoiceField(label = 'Ваш пол',
                               choices = [('1', 'Мужской'), ('2', 'Женский')],
                               widget = forms.RadioSelect, initial = 1)
    internet = forms.ChoiceField(label = 'Как часто вы пользуетесь интернетом',
                                 choices = (('1', 'Каждый день'),
                                            ('2', 'Несколько раз в день'),
                                            ('3', 'Несколько раз в неделю'),
                                            ('4', 'Несколько раз в месяц')), initial = 1)
    notice = forms.BooleanField(label = 'Получать новости с сайта на e-mail?',
                                required = False)
    email = forms.EmailField(label = 'Ваш e-mail', min_length = 7)
    message = forms.CharField(label = 'Коротко о себе',
                              widget = forms.Textarea(attrs = {'rows':12, 'cols':20}))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text': "Комментарий"} #метка к полю формы text





class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title','description','content','posted','image', 'author')
        #author = forms.ModelChoiceField(queryset = User.objects.all())
        labels = {'title': "Заголовок", 'description':"Краткое описание", 'content':"Содержание", 'posted':"Дата",'image':"Картинка"}

        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control", "placeholder": "Заголовок статьи"}),
            'description': forms.Textarea(attrs={"class": "form-control", "placeholder": "Краткое содержание"}),
            'content' : forms.Textarea(attrs={"class": "form-control", "placeholder": "Полное содержание"}),
            'posted' : forms.DateInput(format="%d.%m.%Y %H:%M:%S", attrs={"class": "form-control","value": datetime.datetime.strftime(datetime.datetime.now(), format="%d.%m.%Y %H:%M"),"type": "datetime", }),
            'image': forms.FileInput(),
            'author' : forms.Select(attrs={"class":"form-control"}),
            
            }


class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ('email','text')
        #labels = {'email': "email", 'text': "Вопрос"}


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category','name','slug','image1','image2','image3','case_type','duo_sim','sim_type','system','display_type','resolution','processor','cores','cpu_frequency','gpu','ram','ram_inside','sd','sd_volume_max','main_cam_mp','frontal_cam_mp',
                  'flash','mp3_pleer','recorder','usb_interface','accum_volume','size','weight','description','country','warranty','price','stock','available',)

        widgets = {
            'category':forms.Select(attrs = {"class":"form-control", "placeholder":"Категория"}),
            'name': forms.TextInput(attrs = {"class":"form-control", "placeholder":"Название товара"}),
            'slug': forms.TextInput(attrs = {"class":"form-control", "placeholder":"slug"}),
            'image1': forms.ClearableFileInput(attrs = {"placeholder":"Картинка 1"}),
            'image2': forms.ClearableFileInput(attrs = { "placeholder":"Картинка 2"}),
            'image3': forms.ClearableFileInput(attrs = { "placeholder":"Картинка 3"}),
            'case_type': forms.TextInput(attrs = {"class":"form-control", "placeholder":"Тип корпуса"}),
            'duo_sim': forms.CheckboxInput(),
            'sim_type': forms.TextInput(attrs = {"class":"form-control", "placeholder":"Тип сим-карты"}),
            'system': forms.TextInput(attrs = {"class":"form-control", "placeholder":"Операционная система"}),
            'display_type': forms.TextInput(attrs = {"class":"form-control", "placeholder":"Тип дисплея"}),
            'resolution': forms.TextInput(attrs = {"class":"form-control", "placeholder":"Разрешение экрана"}),
            'processor': forms.TextInput(attrs = {"class":"form-control", "placeholder":"Название процессора"}),
            'cpu_frequency': forms.TextInput(attrs = {"class":"form-control", "placeholder":"Частота прцессора"}),
            'cores': forms.NumberInput(attrs = {"class":"form-control", "placeholder":"Кол-во ядер"}),
            'gpu': forms.TextInput(attrs = {"class":"form-control", "placeholder":"Название видеоускорителя"}),
            'ram': forms.NumberInput(attrs = {"class":"form-control", "placeholder":"ОЗУ"}),
            'ram_inside': forms.NumberInput(attrs = {"class":"form-control", "placeholder":"Кол-во встроенной памяти"}),
            'sd': forms.CheckboxInput(),
            'sd_volume_max': forms.NumberInput(attrs = {"class":"form-control", "placeholder":"Объем sd-карты"}),
            'main_cam_mp': forms.NumberInput(attrs = {"class":"form-control", "placeholder":"Основная камера МП"}),
            'frontal_cam_mp': forms.NumberInput(attrs = {"class":"form-control", "placeholder":"Фронтальная камера МП"}),
            'flash': forms.CheckboxInput(),
            'mp3_pleer': forms.CheckboxInput(),
            'recorder': forms.CheckboxInput(),
            'usb_interface': forms.TextInput(attrs = {"class":"form-control", "placeholder":"USB интерфейс"}),
            'accum_volume': forms.NumberInput(attrs = {"class":"form-control", "placeholder":"Объем аккумулятора мА*ч"}),
            'size': forms.TextInput(attrs = {"class":"form-control", "placeholder":"Размеры ШхВхТ"}),
            'weight': forms.NumberInput(attrs = {"class":"form-control", "placeholder":"Вес в граммах"}),
            'description': forms.TextInput(attrs = {"class":"form-control", "placeholder":"Описание"}),
            'country': forms.TextInput(attrs = {"class":"form-control", "placeholder":"Страна производителя"}),
            'warranty': forms.NumberInput(attrs = {"class":"form-control", "placeholder":"Гарантия (лет)"}),
            'price': forms.NumberInput(attrs = {"class":"form-control", "placeholder":"Стоимость"}),
            'stock': forms.NumberInput(attrs = {"class":"form-control", "placeholder":"Кол-во штук на складе"}),
            'available': forms.CheckboxInput(),
            

            



            
            }
        



                                          
