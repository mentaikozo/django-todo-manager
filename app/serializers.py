from app.models import Task
from rest_framework import serializers


class TagsField(serializers.Field):
    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        return data


class TaskSerializer(serializers.ModelSerializer):
    tags = TagsField(source="get_tags")

    def create(self, validated_data):
        tags = validated_data.pop("get_tags", [])  # タグだけ取り出し
        task = Task.objects.create(**validated_data)
        task.tags.add(*tags)  # taggit にセット
        return task

    def update(self, instance, validated_data):
        tags = validated_data.pop("tags", None)
        print(f"tags: {tags}")
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if tags is not None:
            instance.tags = tags  # タグを更新
        instance.save()
        print(f"instance: {instance}")

        return instance

    class Meta:
        model = Task
        fields = "__all__"
