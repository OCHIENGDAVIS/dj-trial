from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={
        'Placeholder': 'Product title'
    }))
    description = forms.CharField(label='Product Description', widget=forms.Textarea(
        attrs={
            'rows': 4,
            'class': 'desc'
        }
    ))
    price = forms.DecimalField(label='Product Price', initial=200)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if not 'CFE'.lower() in title:
            raise forms.ValidationError('No "CFE" in your title')
        return title


class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={
        'Placeholder': 'Product title'
    }))
    description = forms.CharField(label='Product Description', widget=forms.Textarea(
        attrs={
            'rows': 4,
            'class': 'desc'
        }
    ))
    price = forms.DecimalField(label='Product Price', initial=200)
