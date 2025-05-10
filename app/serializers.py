from app.models import Task
from rest_framework import serializers


class TaskSerializer(serializers.BaseSerializer):
    class Meta:
        model = Task

        fields = [
            'id',
            'name',
            'tags',
            'progress',
            'status',
            'priority',
            'pub_date',
            'notes'
        ]
