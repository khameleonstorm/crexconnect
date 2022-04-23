from django.contrib import admin

# Register your models here.

from .models import Card, Balance


admin.site.register(Card)
admin.site.register(Balance)
