# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Casino, Payment, Software, Currency

class CasinoAdmin(admin.ModelAdmin):  
    list_display = ('name', 'link')

class PaymentAdmin(admin.ModelAdmin):  
    list_display = ('name',)

class SoftwareAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name',)    
    
admin.site.register(Casino, CasinoAdmin)
admin.site.register(Payment, SoftwareAdmin)
admin.site.register(Software, PaymentAdmin)
admin.site.register(Currency, CurrencyAdmin)