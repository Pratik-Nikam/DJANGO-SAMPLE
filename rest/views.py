from django.http import HttpResponse
from rest.models import Category, Product
from rest.serializers import CategorySerializer, ProductSerializer
from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView

@swagger_auto_schema(manual_parameters=[
        openapi.Parameter('ping',
                          openapi.IN_QUERY,
                          description="please input ping",
                          type=openapi.TYPE_STRING)
    ])
def index(request):
    return HttpResponse("Hello, world. You're at the rest index.")


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer




