from django import forms
from .models import TransferWindow


class TransferWindowForm(forms.ModelForm):
    class Meta:
        model = TransferWindow
        fields = [
            'name',
            'age',
            'club',
            'transfer_value',
            'image'
        ]