from django import forms

class Autos_forms(forms.Form):
    name = forms.CharField(max_length= 30)
    description = forms.CharField(max_length= 150)
    price = forms.FloatField()
    SKU = forms.CharField(max_length= 30)
    active = forms.BooleanField()

#class Autos_forms(forms.ModelForm):
#    class Meta:
#        model = Autos
#        fields = "__all__"