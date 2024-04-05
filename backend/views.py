from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from backend.permissions import IsAdminOrReadOnly
from backend.serializers import *
from backend.models import *
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (OrderingFilter, )
    ordering_fields = ('price', )


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminOrReadOnly,)
