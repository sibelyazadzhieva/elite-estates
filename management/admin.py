from django.contrib import admin
from .models import Service, Contract, Ticket

admin.site.register(Service)
admin.site.register(Contract)
admin.site.register(Ticket)