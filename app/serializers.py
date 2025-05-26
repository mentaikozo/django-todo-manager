from app.models import Task
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        many=True,
        slug_field='name', # 名前だけを返す
        read_only=True
    )

    class Meta:
        model = Task
        fields = "__all__"
