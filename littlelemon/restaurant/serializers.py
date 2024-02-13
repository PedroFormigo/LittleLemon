from .models import Menu
from .models import Restaurant
from rest_framework import serializers

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'