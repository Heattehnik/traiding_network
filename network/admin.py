from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from network.models import NetworkNode


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'supplier', 'debt', 'level', 'supplier_link')
    list_filter = ('city',)
    actions = ['clear_debt_to_supplier']

    def supplier_link(self, obj):
        if obj.supplier:
            url = reverse('admin:network_networknode_change', args=[obj.supplier.id])
            return format_html('<a href="{}">Поставщик</a>', url)
        return "Нет поставщика"
    supplier_link.short_description = 'Поставщик'
    supplier_link.allow_tags = True

    def clear_debt_to_supplier(self, request, queryset):
        queryset.update(debt=0)

    clear_debt_to_supplier.short_description = "Очистить задолженность перед поставщиком"
