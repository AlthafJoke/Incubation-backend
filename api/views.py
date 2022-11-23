from django.shortcuts import render, get_object_or_404
from .serializers import ApplicationSerializer, SlotSerializer
from .models import Application, Slot
from rest_framework import viewsets

from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser


# Create your views here.
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        token['admin'] = user.is_superuser
        token['user'] = user.pk
        
        
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class ApplicationViewSet(viewsets.ModelViewSet):
    # queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    
    def get_queryset(self):
        result = Application.objects.filter(Q(status='Pending'))
        
        return result
    
    
    
class StatusUpdate(APIView):
    def put(self, request, pk):
        Application_Instance = get_object_or_404(Application, pk=pk)
        serializer = ApplicationSerializer(Application_Instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
  
class ApplicationApproved(viewsets.ModelViewSet):
    # queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    
    def get_queryset(self):
        result = Application.objects.filter(Q(status='Approved'))
        
        return result


class ApplicationDelete(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class  = ApplicationSerializer
    
    
    
    
class UserApplications(APIView): # this class is used to get application by user id for fetching data to user dashboard
    
    def get(self, request, pk):
        result = Application.objects.filter(user=pk)
        print(result)
        serializser = ApplicationSerializer(result, many=True)
        return Response(serializser.data , status=status.HTTP_200_OK)
    
    

class ApplicationSlot(viewsets.ModelViewSet):
    queryset = Slot.objects.all()
    serializer_class = SlotSerializer
    
    
@api_view(['POST'])
# @permission_classes([IsAdminUser])
def slotAllocate(request, application_id, slot_id):
  slot = Slot.objects.get(id=slot_id)
  applicant = Application.objects.get(id=application_id)
  slot.applicant = applicant
  slot.status = True
  slot.save()
  applicant.is_slot_allotted=True
  applicant.save()
  serializer = SlotSerializer(slot)
  return Response(serializer.data)
    
    
    
    