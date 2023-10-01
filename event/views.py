from .models import *
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from .serializers import *



@api_view(['POST'])
def create_event(request):

    serializer = EventSerializer(data=request.data)
    print(serializer.is_valid())

    if serializer.is_valid():
        # Set the host field to the current user
        serializer.validated_data['host'] = request.user
        serializer.save()
        print(serializer.data)
    else:
        print(serializer.errors)

    return Response({'message':'Created Event Successfully'})


@api_view(['GET'])
def view_events(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)

    return Response(serializer.data)
