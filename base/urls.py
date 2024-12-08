from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from .views import CreateAdsImageListView, CreateAdsSeperate, NewsDataDetailView
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # JWT Authentication
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # News Data
    path('news/', views.get_news_data, name='get_news_data'),  # GET: Fetch all news
    path('news/create/', views.create_news, name='create_news_data'),  # POST: Create news with nested data
    path('news/<str:id>/', NewsDataDetailView.as_view(), name='news-detail'),  # GET: Fetch detailed news by ID

    # Ads Image Management
    path('createadsseperate/', CreateAdsSeperate.as_view(), name='createadsseperate'),  # POST: Create separate ads
    path('getCreatedAds/', CreateAdsImageListView.as_view(), name='ads-image-list'),  # GET: List all ads images
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
