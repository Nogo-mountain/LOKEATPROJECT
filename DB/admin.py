from django.contrib import admin
from .models import Diner
from .models import Menu
from .models import Category
from .models import DinerPicture
from .models import MenuPicture
# Register your models here.

admin.site.register(Diner)
admin.site.register(Menu)
admin.site.register(Category)
admin.site.register(DinerPicture)
admin.site.register(MenuPicture)

