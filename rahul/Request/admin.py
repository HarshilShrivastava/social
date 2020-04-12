from django.contrib import admin
from Request.models import(
    Request,
    Confirmed
)
# Register your models here.
admin.site.register(Confirmed)
admin.site.register(Request)