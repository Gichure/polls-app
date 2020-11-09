from .models import Tenant

def hostname_from_request(request):
    return request.get_host().split(':')[0].lower()

#Used to get the Tenant from a request
def tenant_from_request(request):
    hostname = hostname_from_request(request)
    subdomain_prefix = hostname.split('.')[0]
    return Tenant.objects.filter(subdomain_prefix = subdomain_prefix).first()