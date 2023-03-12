from django.http import Http404

from rest_framework.views import Response
from rest_framework import generics
from rest_framework import status

from .models import Category, Subcategory, Goods
from .serializers import CategorySerializer, SubCategorySerializer, GoodsSerializer


class Menu(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get(self, request, *args, **kwargs):
        slug = kwargs.get('slug', None)
        if not slug:
            return Response({'error': "Method GET not allowed!"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        try:
            queryset = Category.objects.get(slug=slug)
        except:
            raise Http404
        serializer = self.get_serializer_class()

        return Response(serializer(queryset, context={"request": request}).data)
    

class SubcategoryRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubCategorySerializer

    def get(self, request, *args, **kwargs):
        subslug = kwargs.get('subslug', None)
        if not subslug:
            return Response({'error': "Method GET not allowed!"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        try:
            queryset = Subcategory.objects.get(slug=subslug)
        except:
            raise Http404
        serializer = self.get_serializer_class()

        return Response(serializer(queryset, context={"request": request}).data)
    

class GoodsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = GoodsSerializer
    queryset = Goods.objects.filter()

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': "Method GET not allowed!"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        try:
            queryset = Goods.objects.filter(subcategory=pk)
        except:
            raise Http404
        serializer = self.get_serializer_class()
        
        return Response(serializer(queryset, many=True, context={"request": request}).data)
