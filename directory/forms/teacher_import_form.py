import csv
from io import TextIOWrapper

from django import forms

from ..bulk_importer import bulk_insert


class TeacherImportForm(forms.Form):
    CSV = forms.FileField(
        widget=forms.FileInput(
            attrs={'class': 'form-control'}
        ),
        label="Please select a CSV to be imported"
    )

    ZIP = forms.FileField(
        widget=forms.FileInput(
            attrs={'class': 'form-control'}
        ),
        label="Please select the zipped teacher's profile pictures",
        required=False
    )

    def clean(self):
        """Controls file's extension and validity

        Calls the bulk insert function

        Raises:
            forms.ValidationError: In the event of wrong file extension, or
            invalid CSV format

        Returns:
            Validated form fields"""
        csv_file = self.cleaned_data['CSV']
        if not str(csv_file).endswith(".csv"):
            raise forms.ValidationError({"CSV": "Please upload a .csv file"})

        zip_file = self.cleaned_data['ZIP']
        if not str(zip_file).endswith(".zip"):
            raise forms.ValidationError({"ZIP": "Please upload a .zip file"})

        ifile = TextIOWrapper(csv_file, encoding="utf-8")
        csv_reader = csv.reader(ifile, delimiter=',')

        return_value = bulk_insert(csv_reader, zip_file)

        if return_value == 1:
            raise forms.ValidationError(
                {"CSV": "Please provide a valid CSV file"}
            )

        return csv_file, zip_file

    class Meta:
        fields = ["CSV", "ZIP"]
