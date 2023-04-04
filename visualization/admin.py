from django.contrib import admin
from visualization.models import Sales

class SalesAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'price')

admin.site.register(Sales, SalesAdmin)
