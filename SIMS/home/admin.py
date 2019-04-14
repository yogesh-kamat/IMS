from django.contrib import admin

# Register your models here.
from home.models import Supplier, Inventory, Transaction

admin.site.site_header = 'SIMS Admin Panel'
admin.site.register(Supplier)
admin.site.register(Inventory)
admin.site.register(Transaction)
