from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import *
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny

from .serializers import CustomUserSerializer, CategorySerializer, PostSerializer
from app.models import CustomUser, Category, Post
from .permissions import CustomUserPermission, CustomUserDetailsPermission, CategoryPermission, CategoryDetailsPermission, PostPermission, PostDetailPermission


@api_view(['GET', 'POST'])
@permission_classes([CustomUserPermission])
def custom_users(request):
    if request.method == 'GET':
        custom_users = CustomUser.objects.all()
        serializer = CustomUserSerializer(custom_users, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([CustomUserDetailsPermission])
def custom_user_detail(request, pk):
    custom_users = CustomUser.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = CustomUserSerializer(custom_users)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = CustomUserSerializer(custom_users, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        custom_users.delete()
        return Response(status=HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([CategoryPermission])
def category(request):
    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True, context={'request':request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([CategoryDetailsPermission])
def category_detail(request, pk):
    category = Category.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
@permission_classes([PostPermission])
def post(request):
    if request.method == 'GET':
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True, context={'request':request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([PostDetailPermission])
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=HTTP_204_NO_CONTENT)

