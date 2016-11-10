from  django import forms
from .models import Iniciativa



class IniciativaForm(forms.ModelForm):

    class Meta:
        model=Iniciativa

        fields =[

            'num',
            'nombre',
            'turno',
            'comision',
            'resolutivos',
            'enlace',
            'diputado',

        ]

        labels={

            'num':'Numero',
            'nombre':'Nombre',
            'turno':'Turno',
            'comision':'Comision',
            'resolutivos':'Resolutivos',
            'enlace':'Enlace',
            'diputado':'Diputado',

        }
        widgets={

            'num':forms.TextInput(),
            'nombre':forms.TextInput(),
            'turno':forms.TextInput(),
            'comision':forms.TextInput(),
            'olutivos':forms.TextInput(),
            'enlace':forms.TextInput(),
            'diputado':forms.Select(),


        }