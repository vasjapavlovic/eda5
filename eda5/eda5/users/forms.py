from django import forms

from .models import User


class UserCreateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'is_superuser',
            'is_staff',
            'is_active',
        )