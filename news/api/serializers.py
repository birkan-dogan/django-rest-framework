from rest_framework import serializers
from ..models import Article

# without using ModelSerializer
class ArticleSerializer(serializers.Serializer):
    author = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    text = serializers.CharField()
    city = serializers.CharField()
    published_date = serializers.DateField()
    is_active = serializers.BooleanField()
    created_date = serializers.DateTimeField(read_only = True)  # we can see created_date on response object thanks to read_only
    updated_date = serializers.DateTimeField(read_only = True)

    # to handle POST request in serializer, we need a method for that
    def create(self, validated_data):

        return Article.objects.create(**validated_data)
        # in the background, validated_data is a dictionary and we should write like that **validated_data


    # to handle PUT/PATCH request in serializer, we need a method for that too.
    def update(self, instance, validated_data):
        # in PUT request, we take instance and making changes on instance

        instance.author = validated_data.get("author", instance.author)
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.text = validated_data.get("text", instance.text)
        instance.city = validated_data.get("city", instance.city)
        instance.published_date = validated_data.get("published_date", instance.published_date)
        instance.is_active = validated_data.get("is_active", instance.is_active)
        instance.save()

        return instance
