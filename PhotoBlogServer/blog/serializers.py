from blog.models import Post
from rest_framework import serializers
from django.contrib.auth.models import User

#  models 객체와 querysets같은 복잡한 데이터를 JSON, XML과 같은 native 데이터로 바꿔주는 역할

class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Post
        fields = ('author', 'title', 'text', 'created_date', 'published_date', 'image')