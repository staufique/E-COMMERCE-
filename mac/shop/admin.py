from django.contrib import admin
from .models import Product,Contact,Orders,OrdersUpdate
# Register your models here.

class ProductView(admin.ModelAdmin):
    list_display=('product_name','category')

admin.site.register(Product,ProductView)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrdersUpdate)