from django import forms


class CropForm(forms.Form):
    x = forms.IntegerField(max_value=9999, required=True)
    y = forms.IntegerField(max_value=9999, required=True)
    w = forms.IntegerField(max_value=9999, required=True)
    h = forms.IntegerField(max_value=9999, required=True)
    overlay_choice = forms.ChoiceField(choices=(('single', 'single'), ('multiple', 'multiple'),))
    image = forms.ImageField()
