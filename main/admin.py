from django.contrib import admin
from .models import Record


# admin.site.register(Record)
@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    # list_display = ['first_name', 'last_name']
    search_fields = ['first_name__startswith']
