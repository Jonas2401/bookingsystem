from rest_framework import serializers
from .models import Event, Booking, ShareableLink

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class ShareableLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShareableLink
        fields = '__all__'
