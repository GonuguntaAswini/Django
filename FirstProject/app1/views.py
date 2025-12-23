from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.

def view1(request):
    print(request.method)
    return HttpResponse("hello world, i am from view1")

def view2(request):
    return HttpResponse("hello world, i am from view2")

def view3(request):
    return HttpResponse("hello world, i am from view3")

# json always allow object only

def view4(request):
    return JsonResponse({"name":"aswini","message":"hello world"})

def view5(request):
    return JsonResponse({"status":"success","response":"welcome"})

def dynamicview(request):
    qp1=request.GET.get("name",'world')  # getting query param from url
    return HttpResponse(f"hello {qp1}")

def personInfo(request):
    name=request.GET.get("name","aswini")
    role=request.GET.get("role","student")
    city=request.GET.get("city","hyd")
    info={"name":name,"city":city,"role":role}
    return JsonResponse({"status":"success","data":info})


# Task - 16/12/25
# ------------------------------

def movieinfo(request):
    movie=request.GET.get("movie","Akhanda-2")
    showtime=request.GET.get("showtime","6pm")
    ticket_cost=request.GET.get("ticket_cost",250)
    total_no_of_tickets=request.GET.get("total_no_of_tickets",4)
    total_price=request.GET.get("total_price",1000)
    info={"movie":movie,"showtime":showtime,"ticket_cost":ticket_cost,"total_no_of_tickets":total_no_of_tickets,"total_price":total_price}
    return JsonResponse({"status":"success","data":info})



# 17-12-25
# ---------------------

def temp1(request):
    return render(request,"./simple.html")