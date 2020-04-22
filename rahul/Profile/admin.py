from django.contrib import admin
from Profile.models import(
    Profile,
    Status
)
# Register your models here.
admin.site.register(Profile)

admin.site.register(Status)