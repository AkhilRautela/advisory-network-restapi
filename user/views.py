from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import User, Booking
from admin.models import Advisor


import datetime
import jwt


@csrf_exempt
def register_user(req):
    try:
        print(req.headers)
        name = req.POST['name']
        email = req.POST['email']
        password = req.POST['password']
        hashed_password = make_password(password)
        # print(len(hashed_password))
        # print(jwt.encode({"het":"hello"},"secret"))
        # print(len(jwt.encode({"het":"hello"},"secrethg")))
        credentials = {"name": name, "email": email, "password": password}
        token = jwt.encode(credentials, email)
        current_user = User(name=name, email=email, password=hashed_password)
        current_user.save()
        return JsonResponse({"id": current_user.unique_id, "token": token})

    except:

        return HttpResponse(status=400)


@csrf_exempt
def login_user(req):
    try:
        email = req.POST['email']
        password = req.POST['password']
        print(email, password, datetime.datetime.now())
        users = User.objects.get(email=email)
        print(users)
        if check_password(password, users.password):
            # Can't send the same token as it is required from client side to know wethere it is valid or not as token may get expired.
            # I can implement it but I have to build frontened for testing it
            return JsonResponse({"id": users.unique_id}, status=200)
    except:
        return HttpResponse(status=400)
    return HttpResponse(status=400)


def get_advisor(req, user_id):
    try:
        advisors = Advisor.objects.all()
        # print(userid)
        all_advisors = []
        # print(advisors)
        for advisor in advisors:
            all_advisors.append(
                {"name": advisor.name, "url": advisor.url, "id": advisor.unique_id})
        # print(all_advisors)
        return JsonResponse({"advisors": all_advisors})
    except:
        return HttpResponse(status=400)


@csrf_exempt
def book_advisor(req, user_id, advisor_id):
    try:
        booking_time = req.POST['booking-time']
        date_time = datetime.datetime.strptime(booking_time, "%d-%m-%Y %H:%M")
        booking = Booking(
            user_id=user_id, advisor_id=advisor_id, datetime=date_time)
        booking.save()
        User.objects.get(unique_id=user_id)
        Advisor.objects.get(unique_id=advisor_id)
        return HttpResponse(status=200)
    except:
        return HttpResponse(status=400)


def fetch_bookings(req, user_id):
    try:
        user_booking = Booking.objects.filter(user_id=user_id)
        bookings = []
        for x in user_booking:
            # print(x)
            advisor = Advisor.objects.get(unique_id=x.advisor_id)
            now = {
                "advisor name": advisor.name,
                "photo url": advisor.url,
                "User id": x.user_id,
                "Advsor id": x.advisor_id,
                "booking time": str(x.datetime.date())+" "+str(x.datetime.time()),
                "booking id": x.unique_id
            }
            bookings.append(now)
        return JsonResponse({"bookings": bookings}, status=200)
    except:
        return HttpResponse(status=400)


def test(req, userid):
    print(userid)
    return HttpResponse("hello", status=200)
