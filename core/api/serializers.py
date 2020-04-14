from django.contrib.auth.models import User
from rest_framework import serializers
from . import models


"""
This serializer controls how the User is returned and created when called.
"""
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'id']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

"""
This serializer controls how the Profile is returned when called.
"""
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = ['user', 'bio', 'location', 'birth_date', 'score', 'rank']

"""
This serializer controls how the Question is returned when called.
"""
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Question
        fields = '__all__'

"""
This serializer controls how the Trivia Game is returned when called
"""
class TriviaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Trivia
        fields = ['url', 'id', 'created', 'title', 'type', 'category']
