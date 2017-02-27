from django import forms

# potrditev ali žeiliš uvoziti ali ne
class DeliUvozCsvForm(forms.Form):
    skupine_delov_stavbe = forms.BooleanField(initial=False, required=False)
    podskupine_delov_stavbe = forms.BooleanField(initial=False, required=False)


class CsvFilePath(forms.Form):
    csv_file_path = forms.FileField()