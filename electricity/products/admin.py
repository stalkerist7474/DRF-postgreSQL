from django.contrib import admin
from .models import Worker,StoreProducts,ProductParsed,ParsValue

admin.site.register(Worker)
admin.site.register(StoreProducts)
admin.site.register(ProductParsed)
admin.site.register(ParsValue)