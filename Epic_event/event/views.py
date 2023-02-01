

from django.shortcuts import get_object_or_404, render 

# Create your views here.
from django.contrib.auth.models import User

from event.serializers import ClientSerializer, ContractSerializer, EventSerializer, ProfilSerializer, UserTypeSerializer
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.http import HttpRequest
from rest_framework import filters ,status , generics , viewsets
from .models import Client, Contract, Profil, UserGroup ,Event, UserType

from .permissions import IsClientOwnerPermission, IsCommercialPermission, IsContractOwnerPermission, IsEventOwnerPermission
from rest_framework.exceptions import ValidationError


class ClientViewSet(viewsets.ViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = []

    
    def list(self, request):
        queryset = self.queryset.all()
        support_contact = request.query_params.get('support_contact', None)
        event_status = request.query_params.get('event_status', None)
        event_date = request.query_params.get('event_date', None)
        phone = request.query_params.get('phone', None)
        mobile = request.query_params.get('mobile', None)
        date_created = request.query_params.get('date_created', None)
        date_updated = request.query_params.get('date_updated', None)
        sales_contact = request.query_params.get('sales_contact', None)
        company_name = request.query_params.get('company_name', None)
        id = request.query_params.get('id', None)


        if support_contact is not None:
            queryset = queryset.filter(support_contact__id=support_contact)
        if event_status is not None:
            queryset = queryset.filter(event_status=event_status)
        if event_date is not None:
            queryset = queryset.filter(event_date=event_date)
        if phone is not None:
            queryset = queryset.filter(phone=phone)
        if mobile is not None:
            queryset = queryset.filter(mobile=mobile)
        if date_created is not None:
            queryset = queryset.filter(date_created=date_created)
        if date_updated is not None:
            queryset = queryset.filter(date_updated=date_updated)
        if sales_contact is not None:
            queryset = queryset.filter(sales_contact=sales_contact)
        if company_name is not None:
            queryset = queryset.filter(company_name=company_name)
        if id is not None:
            queryset = queryset.filter(id=id)

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
                                                                                                    
        
    def retrieve(self, request, pk=None):
        client = get_object_or_404(Client, id=pk)
        self.check_object_permissions(request, client) 
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    def get_permissions(self):
        print(self.action)
        if self.action in ["update", "retrieve"]:
            print("vous avez la permission !!")

            self.permission_classes = [IsClientOwnerPermission]
        if self.action in [ "create"]:
            self.permission_classes = [IsCommercialPermission]
        return super().get_permissions()

    def create(self, request):
        print(request.data)
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            print("vous cree !!")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        client = get_object_or_404(Client, id=pk)
        self.check_object_permissions(request, client) 
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            print("vous modifier !!")
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        

class EventViewSet(viewsets.ViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['event_status', 'event_date',"email","phone","mobile"]
    """
    Viewset for viewing and editing events.
    """
    def list(self, request):
        queryset = self.queryset.all()
        support_contact = request.query_params.get('support_contact', None)
        event_status = request.query_params.get('event_status', None)
        event_date = request.query_params.get('event_date', None)
        attendees = request.query_params.get('attendees', None)
        note = request.query_params.get('note', None)
        date_created = request.query_params.get('date_created', None)
        date_updated = request.query_params.get('date_updated', None)
        id = request.query_params.get('id', None)
        
        


        if support_contact is not None:
            queryset = queryset.filter(support_contact__id=support_contact)
        if event_status is not None:
            queryset = queryset.filter(event_status=event_status)
        if event_date is not None:
            queryset = queryset.filter(event_date=event_date)
        if attendees is not None:
            queryset = queryset.filter(attendees=attendees)
        if note is not None:
            queryset = queryset.filter(mobile=note)
        if date_created is not None:
            queryset = queryset.filter(date_created=date_created)
        if date_updated is not None:
            queryset = queryset.filter(date_updated=date_updated)
        if id is not None:
            queryset = queryset.filter(id=id)
        
        
        
        

        serializer = self.serializer_class(queryset, many=True)
        print("vous avez lister'!!")
        return Response(serializer.data)



    def retrieve(self, request, pk=None):
        event = get_object_or_404(Event, pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def get_permissions(self):
        print(self.action)
        if self.action in ["update", "retrieve"]:
            print("vous avez la permission !!")
            self.permission_classes = [IsEventOwnerPermission]
        if self.action in [ "create"]:
            self.permission_classes = [IsCommercialPermission]
        return super().get_permissions()


    def create(self, request):
        print(request.data)
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            profil = get_object_or_404(Profil, user=request.user)
            event = serializer.save(support_contact=profil)
            print("vous cree !!")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        event = get_object_or_404(Event, id=pk)
        self.check_object_permissions(request, event) 
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            print("vous modifier !!")
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

class ContractViewSet(viewsets.ViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    filter_backends = [filters.SearchFilter]
 
    """
    Viewset for viewing and editing contracts.
    """
    def list(self, request):
        queryset = self.queryset.all()
        sales_contact = request.query_params.get('sales_contact', None)
        clients = request.query_params.get('clients', None)
        date_created = request.query_params.get('date_created', None)
        date_updated = request.query_params.get('date_updated', None)
        status = request.query_params.get('status', None)
        amount = request.query_params.get('amount', None)
        payment_due = request.query_params.get('payment_due', None)
        event = request.query_params.get('event', None)
        id = request.query_params.get('id', None)
        
        queryset = self.queryset
        if sales_contact is not None:
            queryset = queryset.filter(salescontact=sales_contact)
        if clients is not None:
            queryset = queryset.filter(clients=clients)
        if date_created is not None:
            queryset = queryset.filter(date_created=date_created)
        if date_updated is not None:
            queryset = queryset.filter(date_updated=date_updated)
        if status is not None:
            queryset = queryset.filter(status=status)
        if amount is not None:
            queryset = queryset.filter(amount=amount)
        if payment_due is not None:
            queryset = queryset.filter(payment_due=payment_due)
        if event is not None:
            queryset = queryset.filter(event=event)
        if id is not None:
            queryset = queryset.filter(id=id)
        
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)       

    def retrieve(self, request, pk=None):
        contract = get_object_or_404(Contract, pk=pk)
        serializer = ContractSerializer(contract)
        return Response(serializer.data)

    def get_permissions(self):
        print(self.action)
        if self.action in ["update", "retrieve"]:
            print("vous avez la permission !!")
            self.permission_classes = [IsContractOwnerPermission]
        if self.action in [ "create"]:
            self.permission_classes = [IsCommercialPermission]
        return super().get_permissions()

    def create(self, request):
        serializer = ContractSerializer(data=request.data)
        if serializer.is_valid():
            profil = get_object_or_404(Profil, user=request.user)
            client = Client.objects.get(id=request.data.get('client'))
            contract = serializer.save(sales_contact=profil, client=client)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk=None):
        contract = get_object_or_404(Contract, id=pk)
        self.check_object_permissions(request, contract) 
        serializer = ContractSerializer(contract, data=request.data)
        if serializer.is_valid():
            print("vous modifier !!")
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfilViewSet(viewsets.ViewSet):
    queryset = Profil.objects.all()
    """
    Viewset for viewing and editing profils.
    """
    def list(self, request):
        profils = Profil.objects.all()
        serializer = ProfilSerializer(profils, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        profil = get_object_or_404(Profil, pk=pk)
        serializer = ProfilSerializer(profil)
        return Response(serializer.data)


class UserTypeViewSet(viewsets.ViewSet):
    queryset = UserType.objects.all()
    """
    Viewset for viewing and editing usertypes.
    """
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['type']
    ordering_fields = ['type']

    def list(self, request):
        usertypes = UserType.objects.all()
        serializer = UserTypeSerializer(usertypes, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        usertypes = get_object_or_404(UserType, pk=pk)
        serializer = UserTypeSerializer(usertypes)
        return Response(serializer.data)



