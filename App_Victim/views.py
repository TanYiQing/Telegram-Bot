from datetime import datetime


import App_Victim.models
from django.shortcuts import render
from App_Victim.models import Victim
from django.contrib import messages


def register(request):
    if request.method == "POST":
        dateformat = "%d-%m-%Y"
        ic_no = request.POST["ic_no"]
        name = request.POST["name"]
        hp_no = request.POST["hp_no"]

        ic_year = ic_no[0] + ic_no[1]
        ic_month = ic_no[2] + ic_no[3]
        ic_day = ic_no[4] + ic_no[5]

        current_year = datetime.now().year
        now = str(current_year)[:2]
        if int(now + ic_year) <= current_year:
            year = str((int(now + "00") + int(ic_year)))
        else:
            year = str((int(now + "00") - 100 + int(ic_year)))

        test_date = ic_day + '-' + ic_month + '-' + year
        valid_date = True
        try:
            valid_date = bool(datetime.strptime(test_date, dateformat))
        except ValueError:
            valid_date = False
        print(valid_date)
        if not Victim.objects.filter(ic_no=ic_no).exists():
            if valid_date:
                victim = App_Victim.models.Victim(ic_no=ic_no, name=name, hp_no=hp_no)
                victim.save()
                messages.success(request, "{} registered as victim".format(name))
            else:
                messages.error(request, "Invalid IC number, please try again")
        else:
            messages.error(request, "IC Number registered before")

    return render(request, 'App_Victim/victimregister.html')


def viewdata(request):
    victim_list = Victim.objects.all().order_by("name")
    return render(request, 'App_Victim/viewdata.html', context={'victim_list': victim_list})


def victim_detail(request, ic):
    victim = Victim.objects.get(pk=ic)
    if request.method == "POST":
        hp_no = request.POST["hp_no"]
        victim.hp_no = hp_no
        victim.save()
        respond = "Edit Successful"
        victim_list = Victim.objects.all().order_by("name")
        return render(request, 'App_Victim/viewdata.html', {"status": respond, 'victim_list': victim_list})

    return render(request, 'App_Victim/victimdetails.html', context={'victim': victim})
