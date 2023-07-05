from django import forms
class uforms(forms.Form):
    int1=forms.CharField(label='input-1',widget=forms.TextInput(attrs={"class":"form-control"}))
    int2=forms.CharField(label='input-2',widget=forms.TextInput(attrs={"class":"form-control"}))