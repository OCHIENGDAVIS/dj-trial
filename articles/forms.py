from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)

    def clean_title(self):
        cleaned_data = self.cleaned_data
        print(cleaned_data)
        title = cleaned_data.get('title')
        if 'a' not in title:
            raise forms.ValidationError('title must include the "@" symbol')
        return title

