"""
Definition of forms.
"""

from django import forms
from django.db import models
from .models import Comment
from .models import Blog, Contact
from django.contrib.auth.models import User
import datetime

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
        



                                          
