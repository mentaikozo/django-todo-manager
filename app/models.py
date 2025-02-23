from django.core import validators
from django.db import models
from django.utils import timezone

class Task(models.Model):
    STATUS_CHOICES = (
        (1, "済"),
        (0, "未")
    )

    name = models.CharField(
        verbose_name="タスク名",
        max_length=100
    )

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
        default=timezone.now()
    )
    notes = models.TextField(
        verbose_name="メモ",
        blank=True,
        null=True,
        max_length=50000
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "タスク"
        verbose_name_plural = "タスク"
