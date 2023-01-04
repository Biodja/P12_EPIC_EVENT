from django.db import models
from django.contrib.auth.models import User ,Group


class Profil (models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    user_type = models.ForeignKey("UserType", on_delete=models.CASCADE)


class UserType (models.Model):
    type = models.CharField(max_length=20)



class Contract (models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    user_type = models.ForeignKey("UserType", on_delete=models.CASCADE)


class Client (models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    user_type = models.ForeignKey("UserType", on_delete=models.CASCADE)


class Event (models.Model):
    client = models.ManyToManyField(Client)
    contracts = models.ManyToManyField(Contract)
    user_type = models.ForeignKey("UserType", on_delete=models.CASCADE)


class UserGroup(Group):
    pass
    