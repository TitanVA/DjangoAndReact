from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Pizzeria


class PizzeriaListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pizzeria
        fields = ["id", "pizzeria_name", "city", "zip_code"]


class PizzeriaDetailSerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Pizzeria
        fields = "__all__"

    def get_attribute_url(self, obj):
        return reverse("pizzeria_detail", args=(obj.pk, ))
