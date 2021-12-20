from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from article.api.views import post_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api/post_view/', post_view.as_view({'get': 'list'}), name='post_view'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
