from django.db import models

#modles의 model을 상속받아 class를 만들면 model역할을 하게됨

class Diner(models.Model):
    english_name = models.CharField(max_length=32)
    korean_name = models.CharField(max_length=32)
    email = models.CharField(max_length=64)
    tel = models.CharField(max_length=32)
    area = models.CharField(max_length=32)
    lat = models.CharField(max_length=32,null=True)
    long = models.CharField(max_length=32,null=True)   
    postcode = models.CharField(max_length=32, null=True, blank=True)
    address_1 = models.CharField(max_length=256)
    address_2 = models.CharField(max_length=256)
    operation_time = models.CharField(max_length=128)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    etc = models.TextField(null=True, blank=True)
    # diner_category = 
    
    def __str__(diner):
        return diner.english_name + '' + diner.korean_name
    
class Menu(models.Model):
    english_name = models.CharField(max_length=32)
    korean_name = models.CharField(max_length=32)
    price_won = models.CharField(max_length=32)
    price_dollar = models.CharField(max_length=32)
    explanation = models.CharField(max_length=256)
    etc = models.TextField(null=True, blank=True)
    # menu_category = 
    diner = models.ForeignKey(Diner, on_delete=models.CASCADE, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Category(models.Model):
    name = models.CharField(max_length=32)
    etc = models.TextField(null=True, blank=True)
    category_menus = models.ManyToManyField(Menu, related_name="category")
    # category_diner = models.ManyToManyField(Diner, related_name="category")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class DinerPicture(models.Model):
    label = models.CharField(max_length=32)   
    # 인테리어 익스테리어 lable로 구분하세요
    image = models.ImageField(
        upload_to="diner/images/%Y/%m/%d/%H/",
        blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    

class MenuPicture(models.Model):
    label = models.CharField(max_length=32)
    image = models.ImageField(
        upload_to="menu/images/%Y/%m/%d/%H/",
        blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
