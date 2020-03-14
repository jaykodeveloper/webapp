from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User

class AddUserForm(forms.ModelForm):
    first_password = forms.CharField(
        label='Password', widget=forms.PasswordInput
    )

    confirming_password = forms.CharField(
        label='Confirm password', widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

    def clean_confirming_password(self):
        first_password = self.cleaned_data.get("first_password")
        confirming_password = self.cleaned_data.get("confirming_password")
        if first_password and confirming_password and first_password != confirming_password:
            raise forms.ValidationError("Password does not match")
        return confirming_password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["first_password"])
        if commit:
            user.save()
        return user

class UpdateUserForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = (
            'email', 'password', 'first_name', 'last_name', 'is_active', 'is_staff'
        )

    def clean_password(self):
        return self.initial['passowrd']