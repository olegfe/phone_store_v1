"""
Definition of views.
"""

from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from.forms import AnketaForm
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from .models import Blog
from .models import Comment, Contact
from shop.models import Category
from shop.models import Product
from orders.models import OrderItem, Order
from .forms import CommentForm
from .forms import BlogForm, ContactForm
from django.db.models import Count
from django.shortcuts import render
from app.forms import AddProductForm



def home(request,category_slug=None):
    """Renders the home page."""
    category = None
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
    posts_index = Blog.objects.all()[:3] #запрос на выбор 3 статей для главной страницы
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {'category': category,'categories': categories, 'posts_index': posts_index}
    )

def contact(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug) #выводим названия категорий из базы данных
    assert isinstance(request, HttpRequest) 
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
    else:
        form = ContactForm()
    
     
    return render(
        request,
        'app/contact.html', {'category': category,'categories': categories,'form': form}
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'О нас',
            'message':'Информация о нашей компании.',
            'year':datetime.now().year,
        }
    )
def links(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/links.html',
        {
            'title':'Ссылки',
            'message':'Наши партнеры.',
            'year':datetime.now().year,
        }
    )

def anketa(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    data = None
    gender = {'1': 'Мужчина', '2': 'Женщина'}
    internet = {'1': 'Каждый день', '2':'Несколько раз в день', 
               '3':'Несколько раз в неделю', '4':'Несколько раз в месяц'}
    if request.method == "POST":
        form = AnketaForm(request.POST)
        if form.is_valid():
            data = dict()
            data['name'] = form.cleaned_data['name']
            data['city'] = form.cleaned_data['city']
            data['job'] = form.cleaned_data['job']
            data['gender'] = gender[form.cleaned_data ['gender']]
            data['internet'] = internet[form.cleaned_data ['internet']]
            if(form.cleaned_data['notice']== True):
                data['notice'] = 'Да'
            else:
                data['notice'] = 'Нет'
            data['email'] = form.cleaned_data['email']
            data['message'] = form.cleaned_data['message']
            form = None

    else:
        form = AnketaForm()
    return render(
        request,
        'app/anketa.html',
        {
            
            'form':form,
            'data':data,
            
            
           
        }
    )

def registration(request):
    """Рендер страницы регистрации"""
    if request.method == "POST": #после отправки формы
        regform = UserCreationForm(request.POST)
        if regform.is_valid():
            reg_f = regform.save(commit=False)
            reg_f.is_staff = False #запрет на вход в админ раздел
            reg_f.is_active = True #активный пользователь
            reg_f.date_joined = datetime.now() #дата регистрации
            reg_f.last_login = datetime.now() #дата последней авторизации

            regform.save() # сохраняем изменения после добавления полей
            return redirect('home') #переодресация на главную стр после регистрации
    else:
        regform = UserCreationForm() #создание объекта формы для ввода данных
    assert isinstance(request,HttpRequest)
    return render(request, 'app/registration.html', {'regform':regform, 'year':datetime.now().year,})

def blog(request,category_slug=None):
    #comment_count = Comment.objects.annotate(comments=Count('id')).all()
    category = None
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
    posts = Blog.objects.all() #запрос на выбор всех статей из модели
    assert isinstance(request, HttpRequest)
    return render(request,'app/blog.html',{'title':'Полезные статьи','posts':posts,'year':datetime.now().year,'category': category,'categories': categories } )




def blogpost(request,parametr,category_slug=None):
    category = None
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
    post_1 = Blog.objects.get(id=parametr) #запрос на выбор конкретной статьи по параметру
    comments = Comment.objects.filter(post=parametr)
    

    if request.method == "POST": #после отправки данных формы на сервер методом POST
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = request.user
            comment_f.date = datetime.now()
            comment_f.post = Blog.objects.get(id=parametr)
            comment_f.save()
            
            return redirect('blogpost', parametr=post_1.id) #переадресация на ту же стр
    else:
         form=CommentForm() #создание формы для ввода комментария

        
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blogpost.html',
        {
            'category': category,'categories': categories,
            'post_1':post_1, #передача конкретной статьи в шаблон веб стр
            'comments':comments,
            'form':form,
            'year':datetime.now().year,
        }
    )

def newpost(request):
    if request.method == "POST":
        blogform = BlogForm(request.POST, request.FILES)
        if blogform.is_valid():
            blog_f = blogform.save(commit=False)
            blog_f.posted = datetime.now()

            blog_f.save() #сохранение изменения после добавления

            return redirect('blog')
    else:
        blogform = BlogForm()

    assert isinstance(request, HttpRequest)
    return render (
        request,
        'app/newpost.html',
        {
            'blogform':blogform,
            'year': datetime.now().year
            }
        )


def videopost(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/videopost.html',
        {
            'title':'О нас',
            'message':'Информация о нашей компании.',
            'year':datetime.now().year,
        }
    )

def my_orders(request):
    """Renders the about page."""
    orders = Order.objects.filter(nickname=request.user)
   
    
   
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/my_orders.html', {'orders': orders,}
         )


def addproduct(request):
    if request.method == "POST":
        add_product = AddProductForm(request.POST, request.FILES)
        if add_product.is_valid():
            add_p = add_product.save(commit=False)
            

            add_p.save() #сохранение изменения после добавления

            return redirect('addproduct')
    else:
        add_product = AddProductForm()

    assert isinstance(request, HttpRequest)
    return render (
        request,
        'app/add_product.html',
        {
            'add_product':add_product,
            
            }
        )

