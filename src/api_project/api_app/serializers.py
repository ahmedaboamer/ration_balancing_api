from rest_framework import serializers
from . import models

class HelloSerializer(serializers.Serializer):
    """docstring for HelloSerializer."""
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password')
        extra_kwargs={'password':{'write_only':True}}

    def create(self, validated_data):
        user = validated_data['email']
        name = validated_data['name']

        user = models.UserProfile(user,name)
        user.set_password(validated_data['password'])
        user.save()
        return user
