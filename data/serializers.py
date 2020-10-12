from rest_framework import serializers
from data.models import RideDetails


class RideDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = RideDetails
        fields = ('id', 'user_id')