from django.contrib import admin

# Register your models here.
from .models import Call, Object

admin.site.register(Call)
admin.site.register(Object)