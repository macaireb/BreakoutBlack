from django import forms

from store.models.product import Item, CATEGORY_CHOICES, Category


class RequestProductForm(forms.Form):
    category = forms.ChoiceField(widget=forms.Select, choices=CATEGORY_CHOICES, required=False)
    first = forms.CharField(required=False)
    last = forms.CharField(required=False)
    phone = forms.CharField(required=False, max_length=15)
    email = forms.EmailField(required=False)
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4
        }))


class UploadProductForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        exclude = ('album', 'image_url',)

    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4
        }))

    category = forms.ChoiceField(widget=forms.Select, choices=CATEGORY_CHOICES, required=False)

    widgets = {
        'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
    }


class NewCategory(forms.ModelForm):
    class Meta:
        fields = ('name',)
        model = Category

    name = forms.CharField()
