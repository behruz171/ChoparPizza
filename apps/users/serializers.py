from rest_framework import serializers
from .models import *
import re
def validator(value):
    regex = r"^\+998\d{9}$"

    if not re.fullmatch(regex, value):
        raise serializers.ValidationError({"msg": "not a valid phone number"})


class SignUpSerializer(serializers.Serializer):
    phone_number = serializers.CharField(
        max_length=13,
        min_length=13,
        validators=[validator]
    )
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        phone = validated_data.get('phone_number')
        password = validated_data.get('password')
        user = User.objects.filter(phone_number=phone).first()

        if user:
                raise serializers.ValidationError({'msg': 'This phone number is already in use'})
        else:
            user = User.objects.create_user(phone_number=phone, password=password)


        
        return user

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['tokens'] = instance.tokens()
        return data
    

class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(
        validators=[validator], max_length=13, min_length=13
    )
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        phone_number = attrs.get('phone_number')
        password = attrs.get('password')
        user = User.objects.filter(phone_number=phone_number).first()

        if not user:
            raise serializers.ValidationError({"msg": "User does not exist!"})

        if not user.check_password(password):
            raise serializers.ValidationError({"msg": "Password does not match"})
        
        self.instance = user
        return attrs

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['tokens'] = instance.tokens()
        return data


