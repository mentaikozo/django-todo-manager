from django.urls import reverse
import django_tables2 as tables

from .models import Task

class TaskTable(tables.Table):

    name = tables.LinkColumn(
        "app:detail",
        args=[tables.A("pk")],
        attrs={"a": {"class": "text-primary"}}
    )
    progress = tables.Column()
    status = tables.Column()
    priority = tables.Column()
    pub_date = tables.Column()

    class Meta:
        model = Task
        template_name = "django_tables2/bootstrap4.html"
        # queryset = Task.objects.all()
        fields = ("name", "progress", "status", "priority", "pub_date")
        per_page = 10
