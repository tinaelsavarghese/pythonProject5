from django.contrib import admin
from .models import product,Offer
class productAdmin(admin.ModelAdmin):
    list_display = ('name','price')
class OfferAdmin(admin.ModelAdmin):
    list_display = ('code','discount')
# Register your models here.
admin.site.register(product,productAdmin)
admin.site.register(Offer,OfferAdmin)
