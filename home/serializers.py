from rest_framework import serializers
from home.models import Person, Color
from django.contrib.auth.models import User

class RegisterSerializer(serializers.Serializer):
    username=serializers.CharField()
    email=serializers.EmailField()
    password=serializers.CharField()
    
    def validate(self, data):
        if data['username'] and User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError('Username is taken.')
        
        if data['email'] and User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError('email is taken.')
            
        return data
    
    def create(self,validated_data):
        user = User.objects.create(username=validated_data['username'],email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return validated_data

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()
            

class ColorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Color
        fields = ['color_name']

class PeopleSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    class Meta:
        model=Person
        fields="__all__"
        # depth=1
    
    def validate(self, data):
        
        special_characters = "!@#$%^&*()_+-=,<>/?"
        if any(c in special_characters for c in data['name']):
            raise serializers.ValidationError('name cannot conatain special charactor.')
        
        if data['age'] < 18:
            raise serializers.ValidationError('Age should be grater than 18.')
        
        return data
    