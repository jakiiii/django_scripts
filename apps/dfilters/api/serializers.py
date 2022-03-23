from rest_framework import serializers

from apps.dfilters.models import Author, Category, Journal


class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, data):
        return data


class ApiFilterViewSerializers(serializers.ModelSerializer):
    author = StringSerializer(many=False)
    categories = StringSerializer(many=True)

    class Meta:
        model = Journal
        fields = '__all__'
