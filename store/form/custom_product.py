from django import forms
CATEGORY_CHOICES = (
    ('P', "Pants"),
    ('S', "Shoes"),
    ("Sh", "Shirt"),
    ("So", "Socks"),
    ("Sho", "Shorts"),
    ("C", "Child"),
)


class RequestProductForm(forms.Form):
    category = forms.ChoiceField(widget=forms.Select, choices=CATEGORY_CHOICES, required=False)
    # size = forms.CharField(required=False)
    # color = forms.ChoiceField(widget=forms.Select, choices=Item.Color.choices, required=False)
    first = forms.CharField(required=False)
    last = forms.CharField(required=False)
    phone = forms.CharField(required=False, max_length=15)
    email = forms.EmailField(required=False)
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4
        }))
