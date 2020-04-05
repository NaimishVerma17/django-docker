from rest_framework import serializers

from core.models import Tag, Ingredient, Recipe


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


class RecipeSerializers(serializers.ModelSerializer):
    """Serializer for Recipe object"""

    ingredients = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Ingredient.objects.all()
    )
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all()
    )

    class Meta:
        model = Recipe
        fields = ('id', 'title', 'ingredients', 'tags', 'time_minutes',
                  'price', 'link')
        read_only_fields = ('id',)
