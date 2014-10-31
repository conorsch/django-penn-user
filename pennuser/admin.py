from django.contrib.auth.models import User
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import PennUser


class PennUserCreationForm(UserCreationForm):
    """
    Custom form for creating new PennUsers.
    """

    class Meta(UserCreationForm.Meta):
        model = PennUser
        fields = ("username",)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            PennUser.objects.get(username=username)
        except PennUser.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


class PennUserChangeForm(forms.ModelForm):
    """
    Custom form for editing existing PennUser objects.
    """
    class Meta:
        model = PennUser
        fields = ['username', 'email', 'full_name', 'is_staff']


class PennUserAddForm(forms.ModelForm):
    """
    Custom form for adding users via PennKey in the admin interface.
    """
    class Meta:
        model = PennUser
        fields = ['username', 'is_staff']
        help_texts = {
            'username': "Enter the PennKey of the user to add.",
            'is_staff': "Grants ability to approve waitlist requests from students.",
        }


class PennUserAdmin(admin.ModelAdmin):
    """
    Custom user admin for managing PennUser objects in admin interface.
    """
    model = PennUser
    form = PennUserChangeForm
    add_form = PennUserAddForm
    list_display = ('username', 'full_name', 'email', 'is_staff')


admin.site.register(PennUser, PennUserAdmin)
