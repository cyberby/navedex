from rest_framework import routers, serializers, viewsets
from .models import Project
from .models import Naver
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class NaverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Naver
        fields = ['id', 'name', 'birthdate', 'admission_date', 'job_role', 'projects']
        extra_kwargs = {'projects': {'required': False}}
    def get_fields(self, *args, **kwargs):
            fields = super().get_fields(*args, **kwargs)
            request = self.context.get('request')
            if request is not None and request.method == "GET" and request.parser_context.get('kwargs'):
                self.Meta.depth = 1
            if request is not None and not request.parser_context.get('kwargs'):
                if(request.method == "GET"):

                    fields.pop('projects', None)
            return fields
    def create(self, validated_data):
        request = self.context.get('request')
        validated_data.update({"user_id": request.user.id})
        return super().create(validated_data)

class NaverListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Naver
        fields = ['id', 'name', 'birthdate', 'admission_date', 'job_role']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id','name', 'navers']
        extra_kwargs = {'navers': {'required': False}}

    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        request = self.context.get('request')
        if request is not None and request.method == "GET" and request.parser_context.get('kwargs'):
            fields.pop('navers', None)
            fields.update({"navers": NaverListSerializer(many=True, read_only=True)})
        if request is not None and not request.parser_context.get('kwargs'):
            if (request.method == "GET"):
                fields.pop('navers', None)
        return fields

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data.update({"user_id": request.user.id})
        return super().create(validated_data)
