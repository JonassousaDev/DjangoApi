from rest_framework import serializers
from .models import Curse

class CurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curse
        fields = ('id', 'name', 'language', 'price')
