from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .cart import Cart

# 首頁（最新消息）
def home(request):
    return render(request, 'products/home.html')

# 關於我們
def about_us(request):
    return render(request, 'products/about_us.html')

# 麵包須知
def about_bread(request):
    return render(request, 'products/about_bread.html')

# 會員專區
def member(request):
    return render(request, 'products/member.html')

# 商品頁
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

# 🛒 加入購物車
def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product)
    return redirect("cart_detail")  # 加完導向購物車頁或改 product_list

# ❌ 移除購物車商品
def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect("cart_detail")

# 🧺 購物車內容頁
def cart_detail(request):
    #request.session['cart'] = {}  # ← 清空舊格式
    cart = Cart(request)
    return render(request, 'products/cart_detail.html', {'cart': cart})


def remove_one_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.subtract(product)
    return redirect("cart_detail")


