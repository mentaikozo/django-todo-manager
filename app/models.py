import uuid
from django.core import validators
from django.db import models
from django.utils import timezone
import markdown2
from taggit.managers import TaggableManager  # タグ機能をインポート


class Task(models.Model):
    class Meta:
        verbose_name = "タスク"
        verbose_name_plural = "タスク"

    STATUS_CHOICES = (
        (1, "済"),
        (0, "未")
    )

    # id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)

    name = models.CharField(
        verbose_name="タスク名",
        max_length=100,
        unique=True
    )

    tags = TaggableManager(blank=True)

    progress = models.CharField(
        verbose_name = "進捗",
        max_length=4,
        default = "0%"
    )

    status = models.IntegerField(
        verbose_name="ステータス",
        choices=STATUS_CHOICES,
        default=0
    )
    priority = models.IntegerField(
        verbose_name="優先度",
        default=1,
        validators=[
            validators.MinValueValidator(1),
            validators.MaxValueValidator(10)
        ],
        help_text="1~10で設定、10が最優先"
    )
    pub_date = models.DateTimeField(
        verbose_name="登録日",
        auto_now_add=True
    )
    notes = models.TextField(
        verbose_name="メモ",
        blank=True,
        null=True,
        max_length=50000
    )

    def get_tags(self):
        """
        names() is a django-taggit method, returning a ValuesListQuerySet
        (basically just an iterable) containing the name of each tag as a string
        """
        return self.tags.names()


    def render_notes_as_html(self):
        """マークダウンをHTMLに変換して返す"""
        converter = markdown2.Markdown(extras=["tables", "fenced-code-blocks"])
        return converter.convert(self.notes or "")

    def __str__(self):
        return self.name
