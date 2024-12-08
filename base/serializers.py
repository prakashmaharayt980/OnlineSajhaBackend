from rest_framework import serializers
from .models import AdsImage, NewsData, PostImage, CreateAdsImage


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['id', 'image', 'news']


class AdsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdsImage
        fields = ['id', 'image', 'news']


class NewsDataSerializer(serializers.ModelSerializer):
    post_images = PostImageSerializer(many=True, required=False)  # Nested serializer for PostImage
    ads_images = AdsImageSerializer(many=True, required=False)   # Nested serializer for AdsImage

    class Meta:
        model = NewsData
        fields = [
            'id', 'title', 'description', 'type_of_news', 
            'post_by', 'date_created', 'post_images', 'ads_images'
        ]

    def create(self, validated_data):
        # Extract nested data
        post_images_data = validated_data.pop('post_images', [])
        ads_images_data = validated_data.pop('ads_images', [])

        # Create the NewsData instance
        news = NewsData.objects.create(**validated_data)

        # Create related PostImage and AdsImage instances
        for post_image_data in post_images_data:
            PostImage.objects.create(news=news, **post_image_data)
        for ads_image_data in ads_images_data:
            AdsImage.objects.create(news=news, **ads_image_data)

        return news


class CreateAdsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateAdsImage
        fields = ['id', 'title', 'image', 'post_by', 'date_created']
