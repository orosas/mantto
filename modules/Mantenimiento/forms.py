from django import forms

class BusquedaForm(forms.Form):
	q = forms.CharField(label = "Sitio", widget=forms.TextInput(attrs={'placeholder': 'Buscar Sitio'}), max_length=80)