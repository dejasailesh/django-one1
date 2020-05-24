""" from django import forms
from .models import Career,CareerField,Service,ServiceField,BaseContent
from django.contrib.auth.models import User


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = [
            "name",
        ]

        widgets = {
            "name": forms.Textarea(
                attrs={"placeholder": "Write service here..", "rows": "1", "cols": "60"}
            ),
        }
        labels = {
            "name": "",
        }


class CareerForm(forms.ModelForm):
    class Meta:
        model = Career
        fields = [
            "name",
        ]

        widgets = {
            "name": forms.Textarea(
                attrs={"placeholder": "Write service here..", "rows": "1", "cols": "60"}
            ),
        }
        labels = {
            "name": "",
        }


class ServiceFieldForm(forms.ModelForm):
    class Meta:
        model = ServiceField
        fields = ["field"]

class CareerFieldForm(forms.ModelForm):
    class Meta:
        model = CareerField
        fields = ["field"]


class ServiceEditForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"readonly": "readonly"}))
    email = forms.CharField(widget=forms.TextInput(attrs={"readonly": "readonly"}))

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
        ]

 """
