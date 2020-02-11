from rest_framework import serializers

#from .models import Snippet
from .models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id','username','firstname','lastname', 'title', 'code', 'linenos', 'language', 'style']

from django.contrib.auth.models import User


#Adding endpoints for our User models
class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']
        #Updating our serializer
        owner = serializers.ReadOnlyField(source='owner.username')