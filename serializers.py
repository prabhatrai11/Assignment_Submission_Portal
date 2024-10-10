from rest_framework import serializers
from .models import User, Assignment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'is_admin']

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['user', 'task', 'admin', 'status', 'created_at']
