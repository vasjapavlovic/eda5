from django import forms

class CsvFilePath(forms.Form):
    csv_file_path = forms.FileField()