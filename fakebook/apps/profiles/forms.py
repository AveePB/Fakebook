from django import forms

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