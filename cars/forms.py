
from django import forms

from .models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model=Car
        fields=['brand','model','year','color','price','image']

    def clean_year(self):
        year=self.cleaned_data['year']
        if year<1995:
            raise forms.ValidationError("1995 yildan kattasi qabul qilinmaydi")
        return year