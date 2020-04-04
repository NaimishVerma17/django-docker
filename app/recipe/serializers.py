from rest_framework import serializers

from core.models import Tag


class TagSerializer(serializers.ModelSerializer):
    """Serializers fir tag object"""

    class Meta:
        model = Tag
        field = ('id', 'name')
        read_only_fields = ('id',)
