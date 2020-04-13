from django.urls import path
from vege.views import *

urlpatterns = [
    path('', VegeView.as_view(), name=""),
    path('shop/', ShopView.as_view(), name="shop"),
    path('shop/<int:page_id>', ShopView.as_view()),
    path('wishlist/', WishlistView.as_view(), name="wishlist"),
    path('product-single/', ProductSingleView.as_view(), name="product-single"),
    path('cart/', CartView.as_view(), name="cart"),
    path('checkout/', CheckoutView.as_view(), name="checkout"),
    path('about/', AboutView.as_view(), name="about"),
    path('blog/', BlogView.as_view(), name='blog'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('blog-single/', BlogSingleView.as_view(), name='blog-single'),
]