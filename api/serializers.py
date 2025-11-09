from rest_framework import serializers
from .models import MenuItem, Booking, MenuCategory

class MenuItemSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField() 

    class Meta:
        model = MenuItem
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
