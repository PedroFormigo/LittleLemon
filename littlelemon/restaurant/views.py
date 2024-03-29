from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import viewsets
from .models import Menu
from .models import Restaurant
from .serializers import MenuSerializer
from .serializers import BookingSerializer
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingelMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

@permission_classes([IsAuthenticated])
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = BookingSerializer