from django.contrib import admin
from orders.models import *


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'email_or_phone', 'course', 'created')
