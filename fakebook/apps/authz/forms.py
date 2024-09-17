from django.core.validators import RegexValidator
from django import forms

# Validator to enforce alpha-numeric usernames
alphan_validator = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

class RegisterForm(forms.Form):
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

class LoginForm(forms.Form):
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