from django import forms


class CSVFileUploadForm(forms.Form):
    csv_file = forms.FileField(label='Загрузить CSV файл',
                               widget=forms.FileInput(attrs={'class': 'form-label'})
                               )

    def clean_csv_file(self):
        csv_file = self.cleaned_data['csv_file']
        if not csv_file.name.endswith('.csv'):
            raise forms.ValidationError('Пожалуйста, загрузите файл CSV')
        return csv_file