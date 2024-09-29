from django import forms

class MessageForm(forms.Form):
    content = forms.CharField(
        min_length=1,
        max_length=512,
        required=True,
        error_messages={
            'required': 'Message content is required.',
            'min_length': 'Message cannot be empty.',
            'max_length': 'First name cannot exceed 512 characters.',
        }
    )
