from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm

from app.models import Task


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["name","status","pub_date","notes"]
