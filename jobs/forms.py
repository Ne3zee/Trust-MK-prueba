from django import forms

from .models import Application


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            "full_name",
            "phone",
            "email",
            "age",
            "sales_experience",
            "availability",
            "additional_comments",
        ]
        widgets = {
            "full_name": forms.TextInput(attrs={"placeholder": "Ej: Camila Rojas"}),
            "phone": forms.TextInput(attrs={"placeholder": "+56 9 1234 5678"}),
            "email": forms.EmailInput(attrs={"placeholder": "correo@ejemplo.com"}),
            "age": forms.NumberInput(attrs={"min": 18, "max": 70}),
            "sales_experience": forms.Textarea(attrs={"rows": 4}),
            "additional_comments": forms.Textarea(attrs={"rows": 3}),
        }

    def clean_age(self):
        age = self.cleaned_data["age"]
        if age < 18:
            raise forms.ValidationError("La edad mínima para postular es 18 años.")
        return age
