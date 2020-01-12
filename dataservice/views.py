from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from . import models
from django.core import serializers


SPAM_LIST = ['RBC.RoyalBank.Customer.Service.CANADA0780AVX0780@mail186-26.suw21.mandrillapp.com',
             'elhaabundia@gmail.com', 'qq79@edkomb.com']

def check_if_spam(email):
    if models.KnownScamEmails.objects.filter(email=email).exists():
        scam_email = models.KnownScamEmails.objects.get(email=email)
        scam_email.number_encountered = scam_email.number_encountered + 1
        scam_email.save()
        return True
    return False

def index(request):
    potentials = models.PotentialScamEmail.objects.all()
    knowns = models.KnownScamEmails.objects.all()
    context = {
        "potentials":potentials,
        "knowns": knowns
    }
    return render(request, "index.html", context)

@csrf_exempt
def create_potential_scam_emails(request):
    input = json.loads(request.body)
    for email in input:
        models.PotentialScamEmail.objects.get_or_create(email=email)
        potential_scam_email = models.PotentialScamEmail.objects.get(email=email)
        potential_scam_email.number_encountered = potential_scam_email.number_encountered + 1
        potential_scam_email.save()
        if potential_scam_email.number_encountered > 3:
            models.KnownScamEmails.objects.get_or_create(email=email)
            check_if_spam(email)


    return HttpResponse(json.dumps("Complete"))

@csrf_exempt
def create_scam_emails(request):
    input = json.loads(request.body)
    for email in input:
        models.KnownScamEmails.objects.get_or_create(email=email)
    return HttpResponse(json.dumps("Complete"))

@csrf_exempt
def send_emails(request):
    spam_emails = []
    input = json.loads(request.body)
    for email in input:
        if check_if_spam(email):
            spam_emails.append(email)
    r_value = json.dumps(spam_emails)
    return HttpResponse(r_value)

@csrf_exempt
def get_every_scam_email(request):
    emails = []
    spam_emails = models.KnownScamEmails.objects.all()
    for spam_email in spam_emails:
        temp = {}
        temp["email"] = spam_email.email
        temp["count"] = spam_email.number_encountered
        emails.append(temp)
    return_value = json.dumps(emails)
    return HttpResponse(return_value)

