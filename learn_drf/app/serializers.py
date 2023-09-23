from rest_framework import serializers
from rest_framework.serializers import ValidationError
from . import models


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = "__all__"

    def validate(self, data):
        if data["title"] == data["description"]:
            raise ValidationError("Title&description must different")
        return data
