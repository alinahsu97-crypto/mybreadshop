# products/cart.py

from django.conf import settings
from products.models import Product

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart

    # 加入數量（＋）
    def add(self, product, quantity=1):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                "quantity": 0,
                "price": float(product.price)  # 轉 float 避免運算問題
            }
        self.cart[product_id]["quantity"] += quantity
        self.save()

    # 減少數量（－）
    def subtract(self, product, quantity=1):
        product_id = str(product.id)
        if product_id in self.cart:
            self.cart[product_id]["quantity"] -= quantity

            # 如果數量變 0，就刪除項目
            if self.cart[product_id]["quantity"] <= 0:
                del self.cart[product_id]

            self.save()

    # 完全移除商品
    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session.modified = True

    # 讓購物車可迭代
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        for product in products:
            item = self.cart[str(product.id)]
            item["product"] = product
            item["total_price"] = product.price * item["quantity"]
            yield item

    def clear(self):
        self.session["cart"] = {}
        self.save()

    # 計算總金額
    def get_total_price(self):
        return sum(item["quantity"] * float(item["price"]) for item in self.cart.values())
