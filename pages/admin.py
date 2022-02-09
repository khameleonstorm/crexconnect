from django.contrib import admin

# Register your models here.

from .models import Contact, Balance, Bitcoin, Card

class ContactAdmin(admin.ModelAdmin):
  list_display = ('name', 'email', 'country', 'phone')

admin.site.register(Contact, ContactAdmin)

class BitcoinAdmin(admin.ModelAdmin):
  list_display = ('username', 'amount')

class CardAdmin(admin.ModelAdmin):
  list_display = ('username', 'number')

# class BankAdmin(admin.ModelAdmin):
#   list_display = ('username', 'amount', )



admin.site.register(Bitcoin, BitcoinAdmin)
admin.site.register(Card, CardAdmin)
# admin.site.register(Bank, BankAdmin)


admin.site.register(Balance)
