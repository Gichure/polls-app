from django.db import models

# Create your models here.

class Tenant(models.Model):
    name = models.CharField(max_length = 100),
    subdomain_prefix = models.CharField(max_length = 30, unique = True)
    
class TenantAwareModel(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.deletion.CASCADE)
    
    class Meta:
        abstract = True
        
