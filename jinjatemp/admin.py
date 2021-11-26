from django.contrib import admin
from .models import Invoice, InvoiceDetails, Project
# Register your models here.

admin.site.register(Invoice)
admin.site.register(InvoiceDetails)
admin.site.register(Project)
