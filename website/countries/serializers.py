from rest_framework import serializers
from .models import Country


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = [
            "id",
            "name",
            "lpg_locale",
            "lpg_euro",
            "diesel_locale",
            "diesel_euro",
        ]
