from rest_framework import permissions
from django.shortcuts import get_object_or_404
from .models import Client, Profil, Event, Contract , UserType

class ReadOnlyPermission(permissions.BasePermission):
    """
    Allows access only to read-only requests.
    """

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

class IsClientOwnerPermission(permissions.BasePermission):
    message = "Ce n'est pas votre client !!!"

    def has_permission(self, request, view):
        id_event = view.kwargs.get("pk")
        print(id_event)
        if request.method in permissions.SAFE_METHODS:
            return True
        client = get_object_or_404(Client, id=id_event)
        profil = get_object_or_404(Profil, user=request.user)
        print(client.sales_contact)
        print(profil)
        
        return client.sales_contact == profil 


class IsCommercialPermission(permissions.BasePermission):
    message = "vous n'ete pas le commercial"


    def has_permission(self, request, view):
        profil = get_object_or_404(Profil, user=request.user)
        
        print(profil.user_type)
        print(request.user)
        return profil.user_type == UserType.objects.get(pk=2)
            
            

class IsEventOwnerPermission(permissions.BasePermission):
    message = "Ce n'est pas votre événement !!!"
    def has_permission(self, request, view):
        id_event = view.kwargs.get("pk")
        print(id_event)
        if request.method in permissions.SAFE_METHODS:
            return True
        event = get_object_or_404(Event, id=id_event)
        profil = get_object_or_404(Profil, user=request.user)

        print(profil.id)
   
        
        return event.support_contact == profil


class IsContractOwnerPermission(permissions.BasePermission):
    message = "Ce n'est pas votre contrat !!!"
    
    def has_permission(self, request, view):
        id_event = view.kwargs.get("pk")
        if request.method in permissions.SAFE_METHODS:
            return True
        event = get_object_or_404(Contract, id=id_event)
        profil = get_object_or_404(Profil, user=request.user)
        return event.sales_contact.user == profil


class ReadOnlyPermission(permissions.BasePermission):
    message = "Accès en lecture seule"

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return False
