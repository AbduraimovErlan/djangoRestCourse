from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response
from posts.serializers import PostSerializer
from .models import Post

from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view, APIView, permission_classes
from posts.serializers import PostSerializer
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser
from accounts.serializers import CurrentUserPostsSerializer
from .permissions import ReadOnly, AuthorOrReadOnly



@api_view(http_method_names=["GET", "POST"])
@permission_classes([AllowAny])
def homepage(request: Request):
    if request.method == "POST":
        data = request.data
        response = {"message": "Hello world", "data": data}
        return Response(data=response, status=status.HTTP_201_CREATED)
    response = {"message": "Hello world"}
    return Response(data=response, status=status.HTTP_200_OK)


class PostListCreateView(generics.GenericAPIView,
                         mixins.ListModelMixin,
                         mixins.CreateModelMixin):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)
        return super().perform_create(serializer)

    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostRetrieveUpdateDeleteView(generics.GenericAPIView,
                                   mixins.RetrieveModelMixin,
                                   mixins.UpdateModelMixin,
                                   mixins.DestroyModelMixin
                                   ):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [AuthorOrReadOnly]

    def get(self, request: Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request: Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request: Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


@api_view(http_method_names=["GET"])
@permission_classes([IsAuthenticated])
def get_posts_for_current_user(request: Request):
    user = request.user

    serializer = CurrentUserPostsSerializer(instance=user, context={"request": request})
    return Response(data=serializer.data, status=status.HTTP_200_OK)















#
# class PostViewSet(viewsets.ViewSet):
#     def list(self, request: Request):
#         queryset = Post.objects.all()
#         serializer = PostSerializer(instance=queryset, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#













    # @api_view(http_method_names=["GET", "POST"])
    # def homepage(request: Request):
    #     if request.method == "POST":
    #         data = request.data
    #         response = {"message": "Hello world", "data": data}
    #         return Response(data=response, status=status.HTTP_201_CREATED)
    #     response = {"message": "Hello world"}
    #     return Response(data=response, status=status.HTTP_200_OK)
    #
    #
    # @api_view(http_method_names=["GET", "POST"])
    # def list_posts(request: Request):
    #     posts = Post.objects.all()
    #     if request.method == "POST":
    #         data = request.data
    #
    #         serializer = PostSerializer(data=data)
    #
    #         if serializer.is_valid():
    #             serializer.save()
    #             response = {
    #                 "message": "Post Created",
    #                 "data": serializer.data
    #             }
    #             return Response(data=response, status=status.HTTP_201_CREATED)
    #         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    #     serializer = PostSerializer(instance=posts, many=True)
    #
    #     response = {
    #         "massage": "posts",
    #         "data": serializer.data
    #     }
    #
    #     return Response(data=response, status=status.HTTP_200_OK )
    #
    # @api_view(http_method_names=["GET"])
    # def post_detail(request: Request, post_id: int):
    #     post = get_object_or_404(Post, pk=post_id)
    #
    #     serializer = PostSerializer(instance=post)
    #
    #     response = {
    #         "message": "post",
    #         "data": serializer.data
    #     }
    #     return Response(data=response, status=status.HTTP_200_OK)
    #
    #
    #
    # @api_view(http_method_names=["PUT"])
    # def update_post(request: Request, post_id: int):
    #     post = get_object_or_404(Post, pk=post_id)
    #
    #     data = request.data
    #
    #     serializer = PostSerializer(instance=post, data=data)
    #
    #     if serializer.is_valid():
    #         serializer.save()
    #
    #         response = {
    #             "message": "Post updated successfully"
    #         }
    #         return Response(data=response, status=status.HTTP_200_OK)
    #
    #     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # @api_view(http_method_names=["DELETE"])
    # def delete_post(request: Request, post_id: int):
    #     post = get_object_or_404(Post, pk=post_id)
    #
    #     post.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)









    # def retrieve(self, request: Request, pk=None):
    #     post = get_object_or_404(Post, pk=pk)
    #
    #     serializer = PostSerializer(instance=post)
    #
    #     # def homepage(request:HttpRequest):
    #     #     response={"message": "Hello world"}
    #     #     return JsonResponse(data=response)
    #     return Response(data=serializer.data, status=status.HTTP_200_OK)
    #

