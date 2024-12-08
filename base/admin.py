from django.contrib import admin
from .models import NewsData, CreateAdsImage
from .models import PostImage, AdsImage

# Inline admin for PostImage model
class PostImageInline(admin.TabularInline):  # You can also use StackedInline
    model = PostImage
    extra = 1  # Number of empty forms to display by default

# Inline admin for AdsImage model
class AdsImageInline(admin.TabularInline):  # You can also use StackedInline
    model = AdsImage
    extra = 1  # Number of empty forms to display by default

# Custom admin for NewsData model
class NewsDataAdmin(admin.ModelAdmin):
    list_display = ('title', 'type_of_news', 'post_by', 'date_created')
    inlines = [PostImageInline, AdsImageInline]  # Include both image inlines

# Register the models
admin.site.register(NewsData, NewsDataAdmin)  # Register NewsData with custom admin
admin.site.register(PostImage)  # Optionally register PostImage separately (if needed)
admin.site.register(AdsImage)  # Optionally register AdsImage separately (if needed)




admin.site.register(CreateAdsImage)
# Register your models here.
