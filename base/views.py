from re import search
from django.shortcuts import redirect, render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .forms import NewsForm
from .models import NewsData
from .serializers import NewsDataSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination
import logging


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CreateAdsImageSerializer  # Create this serializer
from django.http import JsonResponse
from django.core.paginator import Paginator

from .models import CreateAdsImage


from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import NewsData, PostImage, AdsImage
from .serializers import NewsDataSerializer, PostImageSerializer, AdsImageSerializer
from rest_framework.filters import OrderingFilter
# View to handle GET request for NewsData
@api_view(['GET'])
@permission_classes([AllowAny])
def get_news_data(request):
    # Fetch all news data
    news = NewsData.objects.all()

    # Get ordering from query parameters (default to latest first)
    ordering = request.query_params.get('ordering', '-date_created')
    typeofnews = request.query_params.get('typeofnews', '')
    
    # Apply filtering based on 'typeofnews'
    if typeofnews:
        news = news.filter(type_of_news=typeofnews)
    
    # Apply ordering
    if ordering:
        news = news.order_by(ordering)

    # Pagination parameters
    page = request.query_params.get('page', 1)  # Default to page 1
    limit = int(request.query_params.get('limit', 10))  # Default to 10 items per page
    
    # Use Paginator to handle pagination
    paginator = Paginator(news, limit)
    
    # Get the current page object
    page_obj = paginator.get_page(page)

    # Serialize the paginated news data
    serializer = NewsDataSerializer(page_obj, many=True)

    # Return paginated response
    response_data = {
        'total_count': paginator.count,
        'total_pages': paginator.num_pages,
        'current_page': page_obj.number,
        'limit': limit,
        'data': serializer.data,
      
    }

    return Response(response_data)

# View to handle POST request for creating NewsData
@api_view(['POST'])
@permission_classes([AllowAny])
def create_news(request):
    if request.method == 'POST':
        # Process both the JSON data and files in the form data
        serializer = NewsDataSerializer(data=request.data)
        
        if serializer.is_valid():
            # Save the NewsData instance and related images
            news = serializer.save()  # This will save the NewsData and related images
            
            # Now process any uploaded files for post_images or ads_images
            if 'post_images' in request.FILES:
                for image in request.FILES.getlist('post_images'):
                    PostImage.objects.create(news=news, image=image)
            
            if 'ads_images' in request.FILES:
                for image in request.FILES.getlist('ads_images'):
                    AdsImage.objects.create(news=news, image=image)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewsDataDetailView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, id, format=None):
        try:
            # Fetch the NewsData object by ID
            news_data = NewsData.objects.get(id=id)
            
            # Get related PostImages and AdsImages
            post_images = PostImage.objects.filter(news=news_data)
            ads_images = AdsImage.objects.filter(news=news_data)
            
            # Serialize the related images
            post_images_serializer = PostImageSerializer(post_images, many=True)
            ads_images_serializer = AdsImageSerializer(ads_images, many=True)
            
            # Serialize the NewsData object
            news_data_serializer = NewsDataSerializer(news_data)
            
            # Combine the data in a response
            response_data = {
                "news_data": news_data_serializer.data,
                "post_images": post_images_serializer.data,
                "ads_images": ads_images_serializer.data
            }
            
            return Response(response_data, status=status.HTTP_200_OK)
        except NewsData.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)


class CreateAdsSeperate(APIView):
    """
    View to handle the creation of ads images.
    Requires authentication.
    """
    permission_classes = [AllowAny]  # Only authenticated users can access this view

    def post(self, request, *args, **kwargs):
        serializer = CreateAdsImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(
                {"message": "Post created successfully!", "data": serializer.data,'status':status.HTTP_200_OK},
                status=status.HTTP_200_OK,
            )
        return JsonResponse(
            {"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
        )


class CreateAdsImageListView(APIView):
    """
    View to list all ads images.
    Accessible to all users (no authentication required).
    """
    permission_classes = [AllowAny]  # Anyone can access this view

    def get(self, request, format=None):
        # Fetch all the ads images from the database
        ads_images = CreateAdsImage.objects.all()
        ordering = request.query_params.get('ordering', '-date_created')
     
        if ordering:
         ads_images = ads_images.order_by(ordering)

        page = request.query_params.get('page', 1)  # Default to page 1
        limit = int(request.query_params.get('limit', 10))  # Default to 10 items per page
    
    # Use Paginator to handle pagination
        paginator = Paginator(ads_images, limit)
    
    # Get the current page object
        page_obj = paginator.get_page(page)

    # Serialize the paginated news data
       
        # Serialize the data using CreateAdsImageSerializer
        serializer = CreateAdsImageSerializer(page_obj, many=True)

        # Return the serialized data as a JSON response
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    