from rest_framework import serializers

#from .models import Snippet
from .models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id','username','firstname','lastname', 'title', 'code', 'linenos', 'language', 'style']