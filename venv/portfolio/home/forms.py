from django import forms
from .models import Message

class ContactForm(forms.Form):
    username = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=254)
    subject = forms.CharField(
        max_length=250
    )
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here your message!'
    )

    class Meta:
        model = Message
        fields = (
            'username',
            'email',
            'subject'
            'message'
        )
    

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        subject = cleaned_data.get('subject')
        message = cleaned_data.get('message')
        if not username and not email and not subject and not message:
            raise forms.ValidationError('You have to write something!')
