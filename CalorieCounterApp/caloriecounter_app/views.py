from django.shortcuts import render,redirect
from .models import Food_Taken,Consumer_Info
# Create your views here.

def Home(request):
    if request.method == 'POST':
        Food_Name = request.POST['Food_Name']
        data = Food_Taken.objects.get(Name=Food_Name)
        userinfo = request.user
        data = Consumer_Info(User_Detail = userinfo, Food_Consumed = data)
        data.save()
        foodinfo = Food_Taken.objects.all()
    else:
        foodinfo = Food_Taken.objects.all()
    consumed_foodinfo = Consumer_Info.objects.filter(User_Detail=request.user)
    context={
        'Foodinfo' : foodinfo,
        'Consumed_foodinfo' : consumed_foodinfo
    }
    return render(request,'caloriecounter_app/home.html',context)

def Remove_ConsumedFood(request,id):
    consumed_foodinfo = Consumer_Info.objects.get(id=id)
    if request.method == 'POST':
        consumed_foodinfo.delete()
        return redirect('/')
    return render(request,'caloriecounter_app/remove.html')
        