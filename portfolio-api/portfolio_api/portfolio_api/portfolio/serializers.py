from rest_framework import serializers
from .models import Technology


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ('name', 'description', 'logo', 'inserted_at', 'used_on_this_page')
