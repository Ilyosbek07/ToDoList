from rest_framework import serializers

from movie.models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    desc = serializers.CharField()
    is_active = serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.desc = validated_data.get('desc', instance.desc)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()

        return instance
