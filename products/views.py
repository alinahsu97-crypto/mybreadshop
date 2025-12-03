from django.shortcuts import render
from .models import Product 
from django.shortcuts import get_object_or_404, redirect
from .models import Product

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

def cart_view(request):
    # 這裡暫時先用空購物車測試
    cart_items = []  # 之後會改成從 session 讀取
    total_price = 0
    return render(request, 'products/cart.html', {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, product_id):
    # 1️⃣ 取得商品，如果不存在則返回 404
    product = get_object_or_404(Product, id=product_id)
    # 2️⃣ 從 session 取得購物車，若不存在則用空字典
    cart = request.session.get('cart', {})
    # 3️⃣ 將商品加入購物車（已有則數量 +1，沒有則設為 1）
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    # 4️⃣ 把更新後的購物車存回 session
    request.session['cart'] = cart
    # 5️⃣ 導向商品列表頁（或可以改成購物車頁面）
    return redirect('product_list')