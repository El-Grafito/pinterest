from rest_framework import serializers

from app.models import CustomUser, Category, Post

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'username',
            'password',
        ]
    
    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            image = obj.image.url
            return request.build_absolute_uri(image)
        return None

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        field = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        field = '__all__'