from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # 首頁
    path('about-us/', views.about_us, name='about_us'),
    path('about-bread/', views.about_bread, name='about_bread'),
    path('member/', views.member, name='member'),
    path('products/', views.product_list, name='product_list'),
    path('cart/', views.cart_view, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

]
