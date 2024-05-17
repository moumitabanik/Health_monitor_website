from rest_framework import serializers
from .models import UserHealthData

class UserHealthDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserHealthData
        fields = '__all__'
