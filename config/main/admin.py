from django.contrib import admin
from .models import TransferWindow


@admin.register(TransferWindow)
class TransferWindowAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'age',
        'club',
        'transfer_value',
    )

    search_fields = (
        'name',
        'club',
    )