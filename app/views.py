from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import NewsSerializer
from .models import NewsModel
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .permissions import StaffPermissionClass, AdminPermissionClass, OwnerPermissionClass

# Create your views here.

# class CreateAPiView(APIView):
#     def post(self, request, *args, **kwargs):
#         if str(request.user) != 'AnonymousUser':
#             if request.user.roles == 2:
#                 serializer = NewsSerializer(data=request.data)
#                 if serializer.is_valid():
#                     serializer.save()
#                     return Response(serializer.data)
#                 return Response(serializer.errors)
#             else:
#                 return Response({'msg': 'only staff members can add'})
#         else:
#             return Response({'msg': 'only staff members can add'})

class AppCreateView(generics.CreateAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated, StaffPermissionClass)


# class ListAPiView(APIView):
#     def get(self, request, *args, **kwargs):
#         if str(request.user) == 'AnonymousUser':
#             return Response({'msg': 'Please log in'})
#         all = NewsModel.objects.filter(status=True)
#         serializer = NewsSerializer(all, many=True)
#         return Response(serializer.data)
class AppListApiView(generics.ListAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        return NewsModel.objects.filter(status=True)

# class UpdateStatus(APIView):
#     def patch(self, request, *args, **kwargs):
#         if str(request.user) != 'AnonymousUser':
#             if request.user.roles == 3:
#
#                 news = get_object_or_404(NewsModel, id=kwargs['news_id'])
#                 serializer = NewsSerializer(news, data=request.data, partial=True)
#                 if serializer.is_valid():
#                     serializer.save()
#                     return Response(serializer.data)
#                 return Response(serializer.errors)
#             else:
#                 return Response({'msg': 'only admins change status'})
#
#         return Response({'msg': 'only admins change status'})

class AppUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated, OwnerPermissionClass)
    lookup_field = 'id'