from django import forms


class CursoForm(forms.Form):
    nombre = forms.CharField()
    descripcion = forms.CharField(widget=forms.Textarea, required=False)
    duracion_semanas = forms.IntegerField(min_value=1, initial=4)
    fecha_inicio = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))
    activo = forms.BooleanField(required=False, initial=True)