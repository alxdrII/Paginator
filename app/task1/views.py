from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


# Create your views here.
def get_blog_page(request):
    return HttpResponse('This is blog')


def get_user_page(request):
    return HttpResponse('This is user page')


def product_list(request):
    # получаем все посты
    products = Product.objects.all()

    # создаем пагинатор
    paginator = Paginator(products, 3)  # 3 поста на странице

    # получаем номер страницы, на которую переходит пользователь
    page_number = request.GET.get('page')

    # получаем посты для текущей страницы
    page_products = paginator.get_page(page_number)

    # передаем контекст в шаблон
    return render(request, 'product_list.html', {'page_products': page_products, 'paginator': paginator})
