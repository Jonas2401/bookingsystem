from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Event, Booking, ShareableLink
from .utils.calendar_utils import get_free_slots
from .services.caldav_service import fetch_events
from .permissions import IsOwnerOrReadOnly
import secrets

@api_view(['POST'])
def book_slot(request):
    user = request.user
    start_time = request.data['start_time']
    end_time = request.data['end_time']
    priority = request.data['priority']

    overlapping_events = Event.objects.filter(
        start_time__lt=end_time, end_time__gt=start_time, user=user)
    
    if overlapping_events.exists() and user.is_authenticated:
        event = Event(user=user, start_time=start_time, end_time=end_time, priority=priority)
        event.save()
    elif not overlapping_events.exists():
        event = Event(user=user, start_time=start_time, end_time=end_time, priority=priority)
        event.save()
    
    return Response({'status': 'Booked'})

@api_view(['POST'])
def generate_link(request):
    limit = request.data['limit']
    token = secrets.token_urlsafe(16)
    link = ShareableLink(token=token, limit=limit)
    link.save()
    return Response({'token': token})
