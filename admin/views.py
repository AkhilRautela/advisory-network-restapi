from django.shortcuts import render
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from .models import Advisor
from user.models import Booking, User
# Create your views here.


@csrf_exempt
def add_advisor(req):
    try:
        advisor_name = req.POST['name']
        advisor_photo_url = req.POST['url']
        here = Advisor(name=advisor_name, url=advisor_photo_url)
        here.save()
        # print(Advisor.objects.all().count())
        # Advisor.objects.all().delete()
        return HttpResponse(status=200)
    except:
        return HttpResponse(status=400)


def truncate_tables(req):
    try:
        User.objects.all().delete()
        Advisor.objects.all().delete()
        Booking.objects.all().delete()
        return HttpResponse(status=200)
    except:
        return HttpResponse(status=400)
