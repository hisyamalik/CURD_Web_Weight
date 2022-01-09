from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import modelBodyWeight

class weightForm(ModelForm):
    class Meta:
        model =  modelBodyWeight
        fields = ('tanggal', 'max_val', 'min_val')
        labels = {
            'tanggal': _('Tanggal'),
            'max_val': _('Berat Max'),
            'min_val': _('Berat Min')
        }
        error_messages = {
            'tanggal': {
                'required': _("Judul harus diisi."),
            },
            'max_val': {
                'required': _("Deskripsi harus diisi."),
            },
            'min_val': {
                'required': _("Deskripsi harus diisi."),
            },            
        }