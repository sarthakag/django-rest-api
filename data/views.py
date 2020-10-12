from django.http import HttpResponse
from data.models import RideDetails
from data.serializers import RideDetailsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@api_view(['GET', 'POST'])
def data(request):
    if request.method == 'GET':
        rides = RideDetails.objects.all()
        serializer = RideDetailsSerializer(rides, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':

        # data = {'id': request.data.get('id'), 'user_id': request.data.get('user_id')}
        # serializer = RideDetailsSerializer(data=data)
        serializer = RideDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getdatabyId(request,id):
    if request.method == 'GET':
        rides = RideDetails.objects.get(id=id)
        serializer = RideDetailsSerializer(rides)
        return Response(serializer.data)
    