from django.shortcuts import render, redirect
from django.views.generic import View
from .settings.base import *
from django.urls import reverse
from django.core.paginator import Paginator
from .models import *
from vegefood.settings import LANGUAGE_CODE
from django.http import HttpResponse

# Create your views here.


class VegeView(View):
    def get(self, request):

        products_list = []
        if LANGUAGE_CODE == 'ru':
            for obj in RuProduct.objects.all()[:8]:
                d = dict(name=obj.name, image=obj.image, price=f'{obj.price} руб', discount=obj.discount,
                         price_sale=f'{obj.price_sale} руб')
                products_list.append(d)

        else:
            for obj in EnProduct.objects.all()[:8]:
                d = dict(name=obj.name, image=obj.image, price=f'{obj.price} $', discount=obj.discount,
                         price_sale=f'{obj.price_sale} $')
                products_list.append(d)

        return render(request, 'vege/index.html',
                      {"products": products_list, 'phone_number': PHONE_NUMBER, 'email_mail': EMAIL_MAIL})


class ShopView(View):

    def get(self, request, page_id=1):

        # products_list = [{'name': 'Bell Pepper',
        #              'image': 'vege/images/product-1.jpg',
        #              'price': '$120.00',
        #              'discount': '30%',
        #              'price_sale': '$80.00'},
        #             {'name': 'Strawberry',
        #              'image': 'vege/images/product-2.jpg',
        #              'price': '$120.00'},
        #             {'name': 'Green Beans',
        #              'image': 'vege/images/product-3.jpg',
        #              'price': '$120.00'},
        #             {'name': 'Purple Cabbage',
        #              'image': 'vege/images/product-4.jpg',
        #              'price': '$120.00'},
        #             {'name': 'Tomatoe',
        #              'image': 'vege/images/product-5.jpg',
        #              'price': '$120.00',
        #              'discount': '30%',
        #              'price_sale': '$80.00'},
        #             {'name': 'Brocolli',
        #              'image': 'vege/images/product-6.jpg',
        #              'price': '$120.00'},
        #             {'name': 'Carrots',
        #              'image': 'vege/images/product-7.jpg',
        #              'price': '$120.00'},
        #             {'name': 'Fruit Juice',
        #              'image': 'vege/images/product-8.jpg',
        #              'price': '$120.00'},
        #             {'name': 'Onion',
        #              'image': 'vege/images/product-9.jpg',
        #              'price': '$120.00',
        #              'discount': '30%',
        #              'price_sale': '$80.00'},
        #             {'name': 'Apple',
        #              'image': 'vege/images/product-10.jpg',
        #              'price': '$120.00'},
        #             {'name': 'Garlic',
        #              'image': 'vege/images/product-11.jpg',
        #              'price': '$120.00'},
        #             {'name': 'Chilli',
        #              'image': 'vege/images/product-12.jpg',
        #              'price': '$120.00'}]

        products_list = []
        if LANGUAGE_CODE == 'ru':
            for obj in RuProduct.objects.all():
                d = dict(name=obj.name, image=obj.image, price=f'{obj.price} руб', discount=obj.discount,
                         price_sale=f'{obj.price_sale} руб')
                products_list.append(d)

        else:
            for obj in EnProduct.objects.all():
                d = dict(name=obj.name, image=obj.image, price=f'{obj.price} $', discount=obj.discount, price_sale=f'{obj.price_sale} $')
                products_list.append(d)

        paginator = Paginator(products_list, 4)
        try:
            products = paginator.page(page_id)
            products.num_pages_tuple = tuple(range(paginator.num_pages))
        except:
            return redirect(reverse('shop'))

        return render(request, 'vege/shop.html',
                      {'products': products, 'phone_number': PHONE_NUMBER, 'email_mail': EMAIL_MAIL})


class WishlistView(View):
    def get(self, request):

        products_list = []
        if LANGUAGE_CODE == 'ru':
            for obj in RuProduct.objects.all()[:6]:
                d = dict(name=obj.name, image=obj.image, price=f'{obj.price} руб', discount=obj.discount,
                         price_sale=f'{obj.price_sale} руб')
                products_list.append(d)

        else:
            for obj in EnProduct.objects.all()[:6]:
                d = dict(name=obj.name, image=obj.image, price=f'{obj.price} $', discount=obj.discount,
                         price_sale=f'{obj.price_sale} $')
                products_list.append(d)

        return render(request, 'vege/wishlist.html',
                      {"products": products_list, 'phone_number': PHONE_NUMBER, 'email_mail': EMAIL_MAIL})


class ProductSingleView(View):
    def get(self, request):
        return render(request, 'vege/product-single.html',
                      {'phone_number': PHONE_NUMBER, 'email_mail': EMAIL_MAIL})


class CartView(View):
    def get(self, request):
        return render(request, 'vege/cart.html',
                      {'phone_number': PHONE_NUMBER, 'email_mail': EMAIL_MAIL})


class CheckoutView(View):
    def get(self, request):
        return render(request, 'vege/checkout.html',
                      {'phone_number': PHONE_NUMBER, 'email_mail': EMAIL_MAIL})


class AboutView(View):
    def get(self, request):
        return render(request, 'vege/about.html',
                      {'phone_number': PHONE_NUMBER, 'email_mail': EMAIL_MAIL})


class BlogView(View):
    def get(self, request):
        # blogs = [{'name': 'Admin',
        #           'image': 'vege/images/image_1.jpg',
        #           'date': 'July 20, 2019',
        #           'head_text': 'Even the all-powerful Pointing has no control about the blind texts',
        #           'text': 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.'},
        #          {'name': 'Marketing Manager',
        #           'image': 'vege/images/image_2.jpg',
        #           'date': 'July 20, 2019',
        #           'head_text': 'Even the all-powerful Pointing has no control about the blind texts',
        #           'text': 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.'},
        #          {'name': 'Interface Designer',
        #           'image': 'vege/images/image_3.jpg',
        #           'date': 'July 20, 2019',
        #           'head_text': 'Even the all-powerful Pointing has no control about the blind texts',
        #           'text': 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.'},
        #          {'name': 'UI Designer',
        #           'image': 'vege/images/image_4.jpg',
        #           'date': 'July 20, 2019',
        #           'head_text': 'Even the all-powerful Pointing has no control about the blind texts',
        #           'text': 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.'},
        #          {'name': 'Web Developer',
        #           'image': 'vege/images/image_5.jpg',
        #           'date': 'July 20, 2019',
        #           'head_text': 'Even the all-powerful Pointing has no control about the blind texts',
        #           'text': 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.'},
        #          {'name': 'System Analyst',
        #           'image': 'vege/images/image_6.jpg',
        #           'date': 'July 20, 2019',
        #           'head_text': 'Even the all-powerful Pointing has no control about the blind texts',
        #           'text': 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.'}
        #          ]

        blogs = []
        if LANGUAGE_CODE == 'ru':
            for object in RuBlog.objects.all():
                d = dict(image=object.image, date=object.date, name=object.name, head_text=object.head_text,
                         text=object.text)
                blogs.append(d)
        else:
            for object in Blogs.objects.all():
                d = dict(image=object.image, date=object.date, name=object.name, head_text=object.head_text, text=object.text)
                blogs.append(d)

        return render(request, 'vege/blog.html',
                      {'blogs': blogs, 'phone_number': PHONE_NUMBER, 'email_mail': EMAIL_MAIL})


class ContactView(View):
    def get(self, request):
        return render(request, 'vege/contact.html',
                      {'phone_number': PHONE_NUMBER, 'email_mail': EMAIL_MAIL, 'website': WEBSITE})


class BlogSingleView(View):
    def get(self, request):
        return render(request, 'vege/blog-single.html',
                      {'phone_number': PHONE_NUMBER, 'email_mail': EMAIL_MAIL})
