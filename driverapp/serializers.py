from rest_framework import serializers
from driverapp.models import DriverRegister

from rest_framework import serializers
from .models import DriverRegister

class DriverRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverRegister
        fields = '__all__'


from rest_framework import serializers
from userapp.models import ComplaintRegister

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplaintRegister
        fields = '__all__'
