from rest_framework import serializers
from ..models import Article, Writer

from datetime import datetime, date
from django.utils.timesince import timesince

# with using ModelSerializer
class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = "__all__"  # fields = ["author", "title", "description"]
        read_only_fields = ["id", "created_date", "updated_date"]

    # adding new field to our serializer without doing anything in views or models
    time_since_pub = serializers.SerializerMethodField()

    """
    author = serializers.StringRelatedField() --> to see author's first_name and last_name instead of author's id, but this will not work when we post author field.

    author = WriterSerializer()  --> this will not work when we want to create an author

    """

    def get_time_since_pub(self, object):
        now = datetime.now()
        pub_date = object.created_date
        if(object.is_active):
            time_delta = timesince(pub_date, now)
            return time_delta

        else:
            return "It is deactive"

    # field validation with ModelSerializer
    def validate_created_date(self, value):
        today = date.today()

        if(value > today):
            raise serializers.ValidationError(f"{value} cannot be bigger than today's date")

        return value


class WriterSerializer(serializers.ModelSerializer):

    # articles = ArticleSerializer(read_only = True, many = True)  # If article is read_only, we can create a new Writer without articles

    articles = serializers.HyperlinkedRelatedField(
        many = True,
        read_only = True,
        view_name = "article-detail",
        # HyperlinkedRelatedField requires the request in the serializer context. Add `context={"request":request} when instantiating the serializer`
    )

    class Meta:
        model = Writer
        fields = "__all__"



# without using ModelSerializer
class ArticleDefaultSerializer(serializers.Serializer):
    id = serializers.CharField()
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


    def validate(self, data):
        # title and description cannot be the same text

        if(data["title"] == data["description"]):
            raise serializers.ValidationError("Title and Description cannot be the same text")

        return data

    # Title need minimum 20 characters
    def validate_title(self, value):

        if(len(value) < 20):
            raise serializers.ValidationError(f"Title need minimum 20 characters, at least enter {20 - len(value)} character")

        return value