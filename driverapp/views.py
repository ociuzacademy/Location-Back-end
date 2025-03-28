from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from driverapp.models import DriverRegister
from driverapp.serializers import DriverRegisterSerializer

from rest_framework import viewsets
from .models import DriverRegister
from .serializers import DriverRegisterSerializer

class DriverRegisterViewSet(viewsets.ModelViewSet):
    queryset = DriverRegister.objects.all().order_by('-id')
    serializer_class = DriverRegisterSerializer
    http_method_names = ['post']  # Restricting to only POST requests

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from driverapp.models import DriverRegister

class DriverLoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            driver = DriverRegister.objects.get(email=email)

            # Check if the entered password matches the stored password
            if driver.password != password:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

            # Check if the driver is approved
            if driver.status != 'approved':
                return Response({'error': 'Your account is not approved'}, status=status.HTTP_403_FORBIDDEN)

            return Response({'message': 'Login successful', 'driver_id': driver.id, 'name': driver.name,'role':'driver',"email":driver.email,"password":driver.password}, status=status.HTTP_200_OK)

        except DriverRegister.DoesNotExist:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from userapp.models import ComplaintRegister
from driverapp.models import DriverRegister
from .serializers import ComplaintSerializer

class DriverComplaintListView(APIView):
    def get(self, request, driver_id):
        try:
            driver = DriverRegister.objects.get(id=driver_id)
            complaints = ComplaintRegister.objects.filter(driver=driver)
            serializer = ComplaintSerializer(complaints, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except DriverRegister.DoesNotExist:
            return Response({"error": "Driver not found"}, status=status.HTTP_404_NOT_FOUND)




from django.shortcuts import render, redirect, get_object_or_404
from userapp.models import ComplaintRegister
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from userapp.models import ComplaintRegister

class UpdateComplaintStatusView(APIView):
    def put(self, request, *args, **kwargs):
        complaint_id = kwargs.get("complaint_id")  # Ensure it matches the URL parameter
        complaint = get_object_or_404(ComplaintRegister, id=complaint_id)

        driver_id = request.data.get("id")

        if driver_id is None:
            return Response({"error": "Driver ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            driver_id = int(driver_id)
        except ValueError:
            return Response({"error": "Invalid Driver ID"}, status=status.HTTP_400_BAD_REQUEST)

        if not complaint.driver or complaint.driver.id != driver_id:
            return Response({"error": "Unauthorized access"}, status=status.HTTP_403_FORBIDDEN)

        complaint.status = request.data.get("status", complaint.status)
        complaint.save()

        return Response({"message": "Complaint status updated successfully"}, status=status.HTTP_200_OK)
