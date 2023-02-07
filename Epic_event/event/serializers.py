

from rest_framework import serializers

from event.models import Contract, Profil, UserType , Event , Client
""""""
class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = ['id', 'type']

class ProfilSerializer(serializers.ModelSerializer):
    user_type = UserTypeSerializer(many=False, read_only=True)
    class Meta:
        model = Profil
        fields = ['id','user','user_type']


class ClientSerializer(serializers.ModelSerializer):
    ##sales_contact = serializers.PrimaryKeyRelatedField(default=serializers.CurrentUserDefault(), queryset=Profil.objects.all())
    
    
    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'mobile', 'company_name', 'date_created', 'date_updated', 'sales_contact']
    
  
  
  
  
  

    
    
    
    

class ContractSerializer(serializers.ModelSerializer):
    

  
    class Meta:
        model = Contract
        fields = ["id",'sales_contact','client','date_created','date_updated','status','amount','payment_due','event']




class EventSerializer(serializers.ModelSerializer):
    client = ClientSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ['id','date_created','date_updated','support_contact','event_status','attendees','event_date','notes','client']
     
    
    
    
    
    
    
    
    
    
    