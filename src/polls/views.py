from django.shortcuts import render
from .models import Poll
from tenants.utils import tenant_from_request;
from django.http import HttpResponse

def index(request):
    return render("Welcome to the Polls App")
         
def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
    response = "You're looking at the results of poll %s."
    return HttpResponse(response % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)           