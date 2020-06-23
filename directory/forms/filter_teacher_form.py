import string

from django import forms

from ..models import Subject

alphabet = list(string.ascii_lowercase)
choices_alphabet = list(map(lambda x: (x, x), alphabet))
choices_subject = list(
    map(lambda x: (x.id, x.name), Subject.objects.all())
)
choices_subject.insert(0, (0, "All"))
choices_alphabet.insert(0, ("all", "No filter"))


class FilterTeacherForm(forms.Form):
    first_name = forms.ChoiceField(
        choices=choices_alphabet,
        widget=forms.Select(attrs={"class": "ml-3 form-control"})
    )

    last_name = forms.ChoiceField(
        choices=choices_alphabet,
        widget=forms.Select(attrs={"class": "ml-3 form-control"})
    )

    subject = forms.ChoiceField(
        choices=choices_subject,
        widget=forms.Select(
            attrs={"class": "ml-3 form-control"}
        ),
        required=False
    )

    class Meta:
        fields = ["first_name", "last_name", "subject", ]
