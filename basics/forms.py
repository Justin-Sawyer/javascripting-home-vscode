from django import forms
from .models import Article, Category
from tinymce.widgets import TinyMCE



class ArticleForm(forms.ModelForm):

    # description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    # description = forms.HTMLField()

    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta():
        model = Article
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_name = [(c.id, c.get_friendly_name()) for c in categories]
        placeholders = {
            'name': 'Name',
            'summary': 'Summary',
            'description': 'Description',
            'script_title_1': 'Script Title',
            'script_1': 'Script URL',
            'codepen_title_1': 'CodePen Title',
            'codepen_data_slug_hash_1': 'CodePen Data Slug Hash',
        }

        for field in self.fields:
            if field != 'category':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
        self.fields['category'].choices = friendly_name
        self.fields['description'].required = True
