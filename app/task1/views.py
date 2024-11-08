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
    # получаем номер страницы, на которую переходит пользователь
    page_number = request.GET.get('page')

    # получаем количество выводимых записей
    count = request.GET.get('count')
    if not count:
        count = '3'

    # получаем все посты
    products = Product.objects.all()

    # создаем пагинатор
    paginator = Paginator(products, int(count))  # 3 поста на странице

    # получаем посты для текущей страницы
    page_products = paginator.get_page(page_number)

    # передаем контекст в шаблон
    context = {
        'page_products': page_products,
        'paginator': paginator,
        'count': count
    }

    return render(request, 'product_list.html', context)
