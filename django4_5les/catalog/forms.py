from django.forms import ModelForm


from catalog.models import Catalog


class CatalogForm(ModelForm):
    class Meta:
        model = Catalog
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CatalogForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
