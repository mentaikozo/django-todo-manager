from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm

from app.models import Task
from django import forms


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["name", "progress", "status", "priority", "notes"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "タスク名"}),
            "progress": forms.TextInput(attrs={"placeholder": "input any%"}),
            "status": forms.RadioSelect(),
            "priority": forms.NumberInput(attrs={"min": 1, "max": 10}),
            "notes": forms.Textarea(attrs={"rows": 3})
        }
