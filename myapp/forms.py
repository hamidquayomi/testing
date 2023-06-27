from django.forms import ModelForm
from .models import Boodschappen

class BoodschappenLijst(ModelForm):
    class Meta:
        model = Boodschappen
        fields = '__all__'
