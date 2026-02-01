from rest_framework import serializers

from .models import Room, RoomImage, OccupiedDate

class RoomImageSerializer(serializers.ModelSerializer):
    room = serializers.HyperlinkedRelatedField(
        view_name = 'room-detail',
        queryset =Room.objects.all()
    )
    class Meta:
        model = RoomImage
        fields = ['id', 'image', 'caption', 'room']   
        


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    images = RoomImageSerializer(many=True, read_only=True)
    class Meta:
        model = Room
        fields = ['url','id','name','type','maxOccupancy','currency','pricePerNight','description', 'images'] 
    
class OccupiedDateSerializer(serializers.HyperlinkedModelSerializer):
    room = serializers.HyperlinkedRelatedField(
        view_name= 'room-detail',
        queryset = Room.objects.all()
    )
    class Meta:
        model = OccupiedDate
        fields = ['url','id','room','date']
