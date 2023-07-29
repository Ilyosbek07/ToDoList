from rest_framework import serializers

from to_do.models import ToDoList


class ToDoListSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    title = serializers.CharField()
    desc = serializers.CharField()
    which_day = serializers.DateField()

    def create(self, validated_data):
        return ToDoList.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.desc = validated_data.get('desc', instance.desc)
        instance.which_day = validated_data.get('which_day', instance.which_day)
        instance.save()

        return instance
