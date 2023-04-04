from django.shortcuts import render

from .models import userModel


# Create your views here.
# def rohit(request):
#     return HttpResponse("hello Ram")

def create(request):
    user_name = 0
    user_email = 0
    mobile_number = 0

    submit = 0
    if request.GET:
        user_name = request.GET["user_name"]
        user_email = request.GET["user_email"]
        mobile_number = request.GET["mobile_number"]
        print("mobile number", mobile_number)

        opt = request.GET["option"]
        ms = userModel()
        ms.user_name = user_name
        ms.user_email = user_email
        ms.mobile_number = mobile_number

        ms.save()
        print("saved")

        if opt == "submit":
            submit = user_name

    return render(request, "create.html",
                  {"user_name": user_name, "user_email": user_email, "mobile_number": mobile_number, "submit": submit})


def retrieve(request):
    users = userModel.objects.all()
    return render(request, "retrieve.html", {'users': users})


def edit(request):
    id = request.GET["id"]
    users = userModel.objects.get(id=id)
    return render(request, 'edit.html', {'users': users})


def update(request):
    id = request.GET["id"]
    users = userModel.objects.get(id=id)
    if request.POST:
        user_name = request.POST["user_name"]
        user_email=request.POST["user_email"]
        mobile_number=request.POST["mobile_number"]
        users.user_name = user_name
        users.user_email =user_email
        users.mobile_number=mobile_number
        users.save()

    return render(request, 'edit.html', {'users': users})


def delete(request):
    if request.GET:
        id = request.GET["id"]
        users = userModel.objects.filter(id=id)[0]
        users.delete()

    return render(request, "delete.html", {"users": users})
#
