from django import forms
from django.core.exceptions import ValidationError
from . import models

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Digite o seu primeiro nome',
            }
        ),
        label='Primeiro Nome',
        help_text='Digite apenas o seu primeiro nome.',
    )
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
        
    #     self.fields['first_name'].widget.attrs.update({
    #         'class':'classe-a classe-b',
    #         'placeholder': 'Escreva aqui',
    #     })
        
    class Meta:
        model = models.Contact
        fields = ('first_name', 'last_name', 'phone',)
        
    def clean(self):
        # cleaned_data = self.cleaned_data
        
        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de Erro',
                code='invalid'
            )
        )
        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem aleatória',
                code='invalid'
            )
        )
        
        return super().clean()