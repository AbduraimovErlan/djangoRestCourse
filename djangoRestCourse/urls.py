
from django.contrib import admin
from django.urls import path, include
from posts.views import PostViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("", PostViewSet, basename="posts")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include(router.urls))
]
