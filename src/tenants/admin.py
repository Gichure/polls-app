from django.contrib import admin
from .utils import tenant_from_request
# Register your models here.
class PollAdmin(admin.ModelAdmin):
    
    fields = ["question","created_by","publication_date"]
    readonly_fields = ["publication_date"]
    
    def get_queryset(self, request, *args, **kwargs):
        queryset = super().get_queryset(request, *args, **kwargs)
        tenant = tenant_from_request(request)
        queryset = queryset.filter(tenant=tenant)
        return queryset

    def save_model(self, request, obj, form, change):
        tenant = tenant_from_request(request)
        obj.tenant = tenant
        super().save_model(request, obj, form, change)