from django.contrib import admin
from .models import Product  # 導入你的模型

# 註冊 Product 模型
admin.site.register(Product)
