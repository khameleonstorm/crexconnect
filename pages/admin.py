from django.contrib import admin

# Register your models here.

from .models import Contact, Balance, Bitcoin

class ContactAdmin(admin.ModelAdmin):
  list_display = ('name', 'email', 'country', 'phone')

admin.site.register(Contact, ContactAdmin)

# class BitcoinAdmin(admin.ModelAdmin):
#   list_display = ('username', 'amount')

# class PaypalAdmin(admin.ModelAdmin):
#   list_display = ('username', 'amount')

# class BankAdmin(admin.ModelAdmin):
#   list_display = ('username', 'amount', )



# admin.site.register(Bitcoin, BitcoinAdmin)
# admin.site.register(Paypal, PaypalAdmin)
# admin.site.register(Bank, BankAdmin)


admin.site.register(Balance)
