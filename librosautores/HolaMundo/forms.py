from django import forms
from HolaMundo.models import Author

class AutorForm (forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'