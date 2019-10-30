from django import forms

class CalculateForm(forms.Form):
    calculation = forms.CharField(label = "Calculation", required = True)