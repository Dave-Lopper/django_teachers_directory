from django import forms

from ..models import Subject, Teacher


class TeacherCreationForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    profile_picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={'class': 'form-control'}
        ),
        required=False
    )
    room = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    subjects = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={"class": "subject_checkboxs"}
        ))

    def clean_subjects(self):
        """Limits selectable subjects to 5

        Raises:
            forms.ValidationError: [description]

        Returns:
            [django.db.models.query.QuerySet]: [Validated subjects]
        """
        subjects = self.cleaned_data['subjects']
        if len(subjects) > 5:
            raise forms.ValidationError(
                "A teacher cannot teach more than 5 subjects."
            )
        return subjects

    class Meta:
        model = Teacher
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone",
            "profile_picture",
            "room",
            "subjects",
        ]
