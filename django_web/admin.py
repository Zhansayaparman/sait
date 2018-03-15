from django.contrib import admin

# Register your models here.
from .models import Kinoteatr,Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name','kinotet')
    fields = ['name', 'kinotet']

admin.site.register(Client, ClientAdmin)
admin.site.register(Kinoteatr)