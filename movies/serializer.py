from rest_framework import serializers
from .models import Movie, ParentalRules


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(
        max_length=10,
        allow_null=True,
        default=None,
    )
    rating = serializers.ChoiceField(
        choices=ParentalRules.choices,
        default=ParentalRules.Rated_G,
    )
    synopsis = serializers.CharField(allow_null=True, default=None)
    added_by = serializers.SerializerMethodField()

    def get_added_by(self, obj: Movie) -> str:
        user = obj.user.email

        return user

    def create(self, validated_data):
        movie = Movie.objects.create(**validated_data)

        return movie
