from rest_framework import serializers
from driverapp.models import DriverRegister

class DriverRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverRegister
        fields = '__all__'
          # Users cannot set status manually

from rest_framework import serializers
from userapp.models import ComplaintRegister

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplaintRegister
        fields = '__all__'
