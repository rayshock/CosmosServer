from django.contrib.auth.models import User, Group

from rest_framework import serializers
from app.models import *
 

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'


class CxSerializer(serializers.ModelSerializer):
   
    #owner = UnitSerializer(many=False, read_only=True)
    owner = 0
    class Meta:
        model = Cx
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    cxs =  CxSerializer(many=True, read_only=True)
    #curCxs = CxSerializer(many=False, read_only=True)
    units = UnitSerializer(many=True, read_only=True)
    class Meta:
        model = GameUser
        fields = '__all__'

 

 

#class GroupSerializer(serializers.HyperlinkedModelSerializer):

#    class Meta:

#        model = Group

#        fields = ('url', 'name')


