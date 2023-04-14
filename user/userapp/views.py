from django.core import serializers
from django.shortcuts import HttpResponse

from .models import userModel


# Create your views here.

def create(request):
    user_name = request.GET["user_name"]
    user_email = request.GET["user_email"]
    mobile_number = request.GET["mobile_number"]
    print("mobile number", mobile_number)

    ms = userModel()
    ms.user_name = user_name
    ms.user_email = user_email
    ms.mobile_number = mobile_number

    ms.save()

    output = serializers.serialize("json", [ms])
    return HttpResponse(output, content_type="application/json")


def jsonall(request):
    output = serializers.serialize("json", userModel.objects.all())
    return HttpResponse(output, content_type="application/json")


# show database record on the server page
def retrieve(request):
    users = userModel.objects.all()
    output = serializers.serialize("json", userModel.objects.all())
    return HttpResponse(output, content_type="application/json")


def edit(request):
    id = request.GET["id"]
    try:
        users = userModel.objects.get(id=id)
        print(users)
        users.user_name = "harsh";
        users.user_email = "subh@123.com";
        users.mobile_number = "8899900556";
        users.save()
        users = [users]
    except:
        return HttpResponse("No data")
    output = serializers.serialize("json", users)
    return HttpResponse(output, content_type="application/json")


def show1data(request):
    id = request.GET["id"]

    users = userModel.objects.get(id=id)
    # users.save()
    users = [users]

    output = serializers.serialize("json", users)
    return HttpResponse(output, content_type="application/json")


def update(request):
    id = request.GET["id"]
    users = userModel.objects.get(id=id)
    try:

        if request.POST:
            user_name = request.POST["user_name"]
            user_email = request.POST["user_email"]
            mobile_number = request.POST["mobile_number"]
            users.user_name = user_name
            users.user_email = user_email
            users.mobile_number = mobile_number

            users.save()
            print(users)
            users = [users]

    except:
        error = {"status": "failed"}
        return HttpResponse("data update")

    output = serializers.serialize("json", users)
    return HttpResponse(output, content_type="application/json")


def delete(request):
    try:
        if request.GET:
            id = request.GET["id"]
            users = userModel.objects.filter(id=id)[0]
            users.delete()
            print(users)
            users = [users]
            output = serializers.serialize("json", users)
            return HttpResponse(output, content_type="application/json")
    except:
        return HttpResponse("no Data")
