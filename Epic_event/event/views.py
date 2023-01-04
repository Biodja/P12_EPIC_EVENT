from django.shortcuts import render
from rules.contrib.views import permission_required
from rules.predicates import is_authenticated
# Create your views here.
from django.contrib.auth.models import User

from .models import Client, UserGroup

def create_group_and_permissions(request):
    # Create user group
    group, created = UserGroup.objects.get_or_create(name='sales')
    
    # Add user to group
    user = User.objects.get(username='john')
    group.user_set.add(user)
    
    # Define permissions for group using django-rules
    
    
    
    @permission_required('sales.view_client', fn=is_authenticated)
    def view_clients(request):
        clients = Client.objects.all()
        return render(request, 'sales/clients.html', {'clients': clients})
    
    return render(request, 'sales/group_created.html')