from django import forms

# our new form
class ContactForm(forms.Form):
    contact_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Email'}), label='')
    