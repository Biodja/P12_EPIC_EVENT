import datetime
from django.db import models
from django.contrib.auth.models import User ,Group


NEW_CONTRACT = 'Nouveau contract'
IN_PROGRESS = 'Contract en cour'
VALIDATED = 'Contract validé'
STATUS_CHOICES = [
(NEW_CONTRACT, 'Nouveau contract'),
(IN_PROGRESS, 'Contract en cour'),
(VALIDATED, 'Contract validé'),
]

class Profil (models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    user_type = models.ForeignKey("UserType", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.user},{self.user_type}'


class UserType (models.Model):
    type = models.CharField(max_length=20 , unique=True)

    def __str__(self) -> str:
        return f'{self.type}'





class Client (models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    company_name = models.CharField(max_length=20)
    date_created = models.DateField(auto_now_add=True, blank=True)
    date_updated = models.DateField(auto_now_add=True , blank=True)
    sales_contact = models.ForeignKey(Profil, on_delete=models.CASCADE , blank=True)
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}{self.sales_contact}'


class EventStatus(models.Model):
    NEW_CONTRACT = 'Nouveau contract'
    IN_PROGRESS = 'Contract en cour'
    VALIDATED = 'Contract validé'
    STATUS_CHOICES = [
        (NEW_CONTRACT, 'Nouveau contract'),
        (IN_PROGRESS, 'Contract en cour'),
        (VALIDATED, 'Contract validé'), ]
    
    status = models.CharField(max_length=20)
    def __str__(self) -> str:
        return f'{self.status}'    

   
   


class Event (models.Model):
    client = models.ManyToManyField(Client , through="Contract" , related_name="client_contract")
    date_created = models.DateField(auto_now_add=True, blank=True)
    date_updated = models.DateField(auto_now_add=True , blank=True)
    support_contact = models.ForeignKey(Profil , on_delete=models.CASCADE , blank=True)
    event_status = models.CharField(max_length=20)
    attendees = models.IntegerField()
    event_date = models.DateTimeField()
    notes = models.TextField()


    def __str__(self) -> str:
        return f'{self.event_status} | {self.date_created} {self.support_contact.user}'

    
class Contract(models.Model):
    sales_contact = models.ForeignKey(Profil, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True, blank=True)
    date_updated = models.DateField(auto_now_add=True , blank=True)  
    status = models.CharField(max_length=20)
    amount = models.FloatField()
    payment_due = models.DateField(auto_now_add=True , blank=True)   
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.client.first_name} | {self.status} '

    
  

class UserGroup(Group):
    pass
    