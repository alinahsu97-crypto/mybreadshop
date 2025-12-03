from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # 首頁
    path('about-us/', views.about_us, name='about_us'),
    path('about-bread/', views.about_bread, name='about_bread'),
    path('member/', views.member, name='member'),
    path('products/', views.product_list, name='product_list'),

    # 🛒 購物車功能
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/minus/<int:product_id>/', views.remove_one_from_cart, name='remove_one_from_cart'),

]
