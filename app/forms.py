from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from taggit.forms import TagField  # タグ用のフィールドをインポート

from app.models import Task
from django import forms


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class TaskForm(ModelForm):
    tags = TagField(required=False)  # タグフィールドを追加

    class Meta:
        model = Task
        fields = ["name", "tags", "progress", "status", "priority", "notes"]  # 必要なフィールドに 'tags' を追加
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "タスク名"}),
            "tags": forms.CharField(
                widget=forms.TextInput(attrs={'placeholder': '例: tag1, tag2, tag3'}),
                help_text='カンマで区切って複数タグを入力'
            ),
            "progress": forms.TextInput(attrs={"placeholder": "input any%"}),
            "status": forms.RadioSelect(),
            "priority": forms.NumberInput(attrs={"min": 1, "max": 10}),
            "notes": forms.Textarea(attrs={'placeholder': 'ここにマークダウンを入力してください✨'})
        }
        labels = {
            "name": "タスク名",
            "tags": "タグ",
            "progress": "進捗",
            "status": "ステータス",
            "priority": "優先度",
            "notes": "メモ",
        }
