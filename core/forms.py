from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', required=True,widget=forms.TextInput(
        attrs={'placeholder':'Escribe tu Nombre'}
    ))
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(
        attrs={'placeholder':'Escribe tu Email'}
    ))
    content = forms.CharField(label='Mensaje', required=True, widget=forms.Textarea(
        attrs={'placeholder':'Escribe tu Mensaje', 'rows':3}
    ))
    
