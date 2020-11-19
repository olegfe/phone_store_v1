from django.shortcuts import render, get_object_or_404,redirect
from .models import Category, Product, Review
from cart.forms import CartAddProductForm
from shop.forms import ReviewForm
from datetime import datetime
from django.http import HttpRequest
#Поиск по сайту




def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})



def product_detail(request, id, slug,category_slug=None):
    category = None
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()


    # отзыв на продукт
    reviews = Review.objects.filter(product=id)
    reviews_count = Review.objects.all()
    if request.method == "POST": #после отправки данных формы на сервер методом POST
        form = ReviewForm(request.POST)
        if form.is_valid():
            review_f = form.save(commit=False)
            review_f.author = request.user
            review_f.date = datetime.now()
            review_f.product = Product.objects.get(id=id)
            review_f.save()
            
            return redirect('shop:product_detail', id=product.id, slug=product.slug,) #переадресация на ту же стр
    else:
         form = ReviewForm() #создание формы для ввода комментария

    assert isinstance(request, HttpRequest)
    return render(request, 'shop/product/detail.html', {'product': product,'form':form,'reviews': reviews,'reviews_count':reviews_count,
                                                        'cart_product_form': cart_product_form,'category': category,'categories': categories})





