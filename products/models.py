from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)           # 商品名稱
    description = models.TextField()                  # 商品介紹
    price = models.DecimalField(max_digits=8, decimal_places=2)  # 價格
    image = models.ImageField(upload_to='products/images/')      # 圖片
    
    def __str__(self):
        return self.name
