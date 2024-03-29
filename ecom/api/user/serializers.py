from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import authentications_classes, permission_classes

from .models import CustomUser

class UserSerializer(serializers.hyperlikedModelSerializer):
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setsttr(instance, attr, value)

        instance.save()
        return instance


    class Meta:
        model = CustomUser
        extra_kwargs = {'password': {'write_only ' :True}}
        fields = ('name', 'email' , 'password', 'gender', 'is_active', 'is_staff', 'is_superuser')