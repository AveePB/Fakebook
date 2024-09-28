from django.core.validators import RegexValidator
from django import forms

# Validator to enforce alpha-numeric usernames
alphan_validator = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

class EmailForm(forms.Form):
    email = forms.EmailField(
        min_length=8,
        max_length=32,
        required=True,
        error_messages={
            'required': 'Email is required.',
            'min_length': 'Email must be at least 8 characters long.',
            'max_length': 'Email cannot exceed 32 characters.',
        }
    )

class PasswordForm(forms.Form):
    password = forms.CharField(
        min_length=8,
        max_length=32,
        widget=forms.PasswordInput(),
        required=True,
        error_messages={
            'required': 'Password is required.',
            'min_length': 'Password must be at least 8 characters long.',
            'max_length': 'Password cannot exceed 32 characters.'
        }
    )

class ImageForm(forms.Form):
    file = forms.ImageField(
        required=True,
        error_messages={
            'required': 'Please upload an image.',
            'invalid_image': 'The uploaded file must be a valid image.'
        }
    )

class BioForm(forms.Form):
    bio = forms.CharField(
        widget=forms.Textarea(),
        required=True,
        error_messages={
            'required': 'Please enter your bio.'
        }
    )

class FirstNameForm(forms.Form):
    first_name = forms.CharField(
        min_length=3,
        max_length=32,
        validators=[alphan_validator],
        required=True,
        error_messages={
            'required': 'First name is required.',
            'min_length': 'First name must be at least 3 characters long.',
            'max_length': 'First name cannot exceed 32 characters.',
            'invalid': 'First name must contain only alphanumeric characters.',
        }
    )

class LastNameForm(forms.Form):
    last_name = forms.CharField(
        min_length=3,
        max_length=32,
        validators=[alphan_validator],
        required=True,
        error_messages={
            'required': 'Last name is required.',
            'min_length': 'Last name must be at least 3 characters long.',
            'max_length': 'Last name cannot exceed 32 characters.',
            'invalid': 'Last name must contain only alphanumeric characters.',
        }
    )