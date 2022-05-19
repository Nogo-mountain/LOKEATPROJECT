from contextlib import nullcontext
from pyexpat.errors import messages
from typing import ItemsView
from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from django.http import JsonResponse
from DB.models import *



#화면에 맛집 표시하기 
def index(request):
    return render (request,'lokeat/index.html','lokeat/diner.html','lokeat/menu.html','lokeat/category.html','test_map/map.html', )

def map(request):
    # recommend_restaurant에 있는 모든 객체를 불러와 recommend_restaurants에 저장
    # recommend_restaurants = recommend_restaurant.object.all()
    # str =''
    return render (request,'test_map/map.html')

#화면에 맛집 표시하기 
#(37.55822352608024,126.92298267805037) 



def test(request):
    create_diner()
    return JsonResponse({})


def index(request):
    return render(request, "menus/index.html")


def create_diner(en_name, ko_name, email, tel, area, lat, long, postcode, add1, add2, menu_id, category_id):

    new_diner = Diner()
    new_diner.en_name = en_name
    new_diner.ko_name = ko_name
    new_diner.email = email
    new_diner.tel = tel
    new_diner. area = area
    new_diner.lat = lat
    new_diner.long = long
    new_diner. postcode = postcode
    new_diner. add1 = add1
    new_diner. add2 = add2
    
    new_diner.menu = get_object_or_404(Menu, id=menu_id)
    new_diner.menu = get_object_or_404(Category, id=category_id)
    
    new_diner.save()
    return {
        "id": new_diner.id,
        "ko_name": new_diner.ko_name,
        "en_name": new_diner.en_name,
        "email": new_diner.email,
        "tel": new_diner.tel,
        "area": new_diner.area,
        "long":new_diner.long,
        "lat":new_diner.lat,
        "postcode": new_diner.postcode,
        "add1": new_diner.add1,
        "add2": new_diner.add2,        
    }

def create_menu(en_name, ko_name, price_won, price_dollor, diner_id, category_id):
    new_menu = Menu()
    new_menu.en_name = en_name
    new_menu.ko_name = ko_name
    new_menu.price_won = price_won
    new_menu.price_dollor = price_dollor
    new_menu.diner = get_object_or_404(Diner, id=diner_id)
    
    new_menu.save()
    return {
        "id": new_menu.id,
        "en_name": new_menu.en_name,
        "ko_name": new_menu.ko_name,
        "price_won": new_menu.price_won,
        "price_dollor": new_menu.price_dollor,
    }
    
def create_category(kind, diner_id, menu_id):
    new_category = Category()
    new_category.kind = kind
    new_category.diner = get_object_or_404(Diner, id=diner_id)
    new_category.menu = get_object_or_404(Menu, id=menu_id)
    new_category.save()
    return {
        "id": new_category.id,
        "kind": new_category.kind,
      
    }    

def diner_picture_file(diner_picture_file, diner_id,):
    new_diner_picture_file = DinerPicture()
    new_diner_picture_file = diner_picture_file()
    
    new_diner_picture_file.diner = get_object_or_404(Diner, id=diner_id)
    new_diner_picture_file.save()
    return {
        "id": new_diner_picture_file.id,
    }   
    
def menu_picture_file(menu_picture_file, menu_id):
    new_menu_picture_file = MenuPicture()
    new_menu_picture_file = menu_picture_file()
    
    new_menu_picture_file.menu = get_object_or_404(Menu, id=menu_id)
    new_menu_picture_file.save()
    return {
        "id": new_menu_picture_file.id,
    }   

def get_menu_diner(menu_id):
    menu = get_object_or_404(Menu, id=menu_id)
    diner = menu.diner
    print(f"this menu is for: {diner.name}")


def get_diner_menus(diner_id):
    diner = get_object_or_404(Diner, id=diner_id)
    menu_list = diner.diner_menus.all()
    for menu in menu_list:
        print(f"this diner has menu: {menu.name}")


def get_diner_categories(diner_id):
    target_diner = get_object_or_404(Diner, id=diner_id)
    diner_categories = target_diner.diner_categories.all()
    for category in diner_categories:
        print(f"the category of this diner: {category.name}")

def get_category_diners(category_id):
    target_category = get_object_or_404(Category, id=category_id)
    category_diners = target_category.category_diners.all()
    for diner in category_diners:
        print(f"diners under this category: {diner.name}")

def set_diner_category(diner_id, category_id):
    target_diner = get_object_or_404(Diner, id=diner_id)
    target_category = get_object_or_404(Category, id=category_id)
    target_category.category_diners.add(target_diner)
    target_category.save()
    
    target_diner.save()
    
def addDiner(request):
    if request.method == "POST":
        new_diner = Diner()
        new_diner.en_name = request.POST.get('en_name')
        new_diner.ko_name = request.POST.get('ko_name')
        new_diner.email = request.POST.get('email')
        new_diner.tel = request.POST.tel('tel')
        new_diner. area = request.POST.area('area')
        new_diner.lat = request.POST.lat('lat')
        new_diner.long = request.POST.long('long')
        new_diner. postcode = request.POST.postcode('postcode')
        new_diner. add1 = request.POST.add1('add1')
        new_diner. add2 = request.POST.add2('add2')
        
        if len(request.FILES) !=0:
            new_diner.image = request.FILES['image']
            
        new_diner.save()
        messages.success(request,"New Diner Added Successfully")
        return redirect('/')
        
    return render(request, 'new_diner/db.html')   

 