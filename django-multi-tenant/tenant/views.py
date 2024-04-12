from django.shortcuts import render

from .utilities import get_tenant
from .models import Tenant

def shape_view(request):
    if request.method == "POST":
        nickname = request.POST.get('nickname-input', 'arjun')
        backstory = request.POST.get('backstory-input', 'an engineering student at the university of waterloo')
        
        t = Tenant(nickname=nickname, backstory=backstory)
        # TODO create custom tagline and background gradient
        # and save in data field on template
        t.save()
        
        
    tenant = get_tenant(request)
    
    print("ARJUN LOG TENANT")
    print(tenant)
    # TODO pull tagline and background gradient if saved and pass to template
    return render(request, 'tenant/shape_page.html', { 'tenant': tenant })
