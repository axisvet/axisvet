from django.contrib import admin
from . models import MyModel
# Register your models here.


class MyModelOptions(admin.ModelAdmin):
    # define the autocomplete_lookup_fields
    autocomplete_lookup_fields = {
        'generic': [['content_type', 'object_id'], ['relation_type', 'relation_id']],
    }

admin.site.register(MyModel, MyModelOptions)