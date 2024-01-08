from django.contrib import admin
from .models import Product,Contact,Orders,OrdersUpdate
# Register your models here.

class ProductView(admin.ModelAdmin):
    list_display=('product_name','category')
    
class OredersAdmin(admin.ModelAdmin):
    list_display=('order_id','email')

admin.site.register(Product,ProductView)
admin.site.register(Contact)
admin.site.register(Orders,OredersAdmin)
admin.site.register(OrdersUpdate)