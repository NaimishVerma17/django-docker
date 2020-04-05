from rest_framework import serializers

from core.models import Tag, Ingredient


class TagSerializer(serializers.ModelSerializer):
    """Serializers for tag object"""

    class Meta:
        model = Tag
        field = ('id', 'name')
        read_only_fields = ('id',)


class IngredientSerializer(serializers.ModelSerializer):
    """Serializers for ingredient object"""

    class Meta:
        model = Ingredient
        field = ('id', 'name')
        read_only_fields = ('id',)
