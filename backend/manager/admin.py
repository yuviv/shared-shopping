from django.contrib import admin
from manager.models import ShoppingList, Profile, Item, IOU

#Register models to show up on admin site to manually configure data
admin.site.register(ShoppingList)
admin.site.register(Profile)
admin.site.register(Item)
admin.site.register(IOU)

