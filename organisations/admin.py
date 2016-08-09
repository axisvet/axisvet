from django.contrib import admin

# Register your models here.
from .models import Company, Practice, Location

admin.site.register(Company)
admin.site.register(Practice)
admin.site.register(Location)