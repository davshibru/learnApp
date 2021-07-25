from rest_framework import serializers
from django.forms import ModelForm
from account.models import Account
from .models import Geniral_Topics, Topics, Lections, UserAccess, UserResults
from rest_framework.validators import UniqueTogetherValidator

class getGeniralTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geniral_Topics
        fields = '__all__'

class getTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topics
        fields = '__all__'



class getIdTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topics
        fields = ['id']


class getIdGeniralTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geniral_Topics
        fields = ['id']

# Lection --------------------------------------------------


class LectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lections
        fields = ['id', 'title', 'body', 'question', 'topics', 'slug']

class LectionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lections
        fields = '__all__'
        lookup_field = 'slug'

class LectionForm(ModelForm):
    class Meta:
        model = Lections
        fields = ['title', 'body', 'question', 'topics']

class LectionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lections
        fields = '__all__'

class UserResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserResults
        fields = '__all__'

        validators = [
            UniqueTogetherValidator(
                queryset=UserResults.objects.all(),
                fields=['account', 'lection'],
                message='такое уже есть'
            )
        ]


class UserResultDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserResults
        fields = '__all__'
        lookup_field = 'sluguser'
#-----------------------------------------------------------

class UserResultSerializer1(serializers.ModelSerializer):
    class Meta:
        model = UserResults
        fields = '__all__'


class UserAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccess
        fields = '__all__'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

        validators = [
            UniqueTogetherValidator(
                queryset=UserAccess.objects.all(),
                fields=['account', 'topics'],
                message='такое уже есть'
            )
        ]









